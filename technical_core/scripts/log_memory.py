#!/usr/bin/env python3
"""
log_memory.py - Registro de aprendizajes y eventos importantes

Este script actualiza automáticamente memory/memory.md con nuevos
aprendizajes, decisiones o eventos que el agente debe recordar.

Uso:
    python log_memory.py add "Título del aprendizaje" "Descripción"
    python log_memory.py update-estado "nuevo estado"
    python log_memory.py config "clave" "valor"
    python log_memory.py list
"""

import os
import sys
from datetime import datetime

MEMORY_FILE = "memory/memory.md"

def read_memory():
    """Lee el contenido actual de memory.md"""
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERR] No se encontró {MEMORY_FILE}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[ERR] Error leyendo memory.md: {e}", file=sys.stderr)
        return None

def write_memory(content):
    """Escribe el contenido actualizado a memory.md"""
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] memory.md actualizado")
    except Exception as e:
        print(f"[ERR] Error escribiendo memory.md: {e}", file=sys.stderr)

def add_entry(titulo, descripcion):
    """Añade un nuevo aprendizaje/evento a memory.md"""
    content = read_memory()
    if content is None:
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M")
    
    # Detectar si hay más de una sección de notas para insertar antes
    marker = "*Última actualización:"
    if marker in content:
        parts = content.split(marker)
        header = parts[0]
        footer = marker + parts[1]
    else:
        header = content
        footer = ""
    
    new_entry = f"""## [{fecha}] {titulo}

### Descripción
{descripcion}

### Acción/Resultado
[Pendiente de completar]

### Referencia
[Sesión: conversaciones/{fecha}_{hora.replace(':', '')}-*.md]

"""
    
    # Insertar antes del footer
    new_content = header + new_entry + footer
    write_memory(new_content)
    return True

def update_fecha():
    """Actualiza la fecha de última modificación"""
    content = read_memory()
    if content is None:
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    # Buscar y actualizar la línea de fecha
    import re
    pattern = r'\*\*Última actualización:\*\* \d{4}-\d{2}-\d{2}'
    replacement = f'**Última actualización:** {fecha}'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content == content:
        # Si no encontró patrón, añadir al inicio
        new_content = content.replace("**Fecha:**", f"**Última actualización:** {fecha}\n**Fecha:**", 1)
    
    write_memory(new_content)
    return True

def add_decision(decision, contexto, resultado):
    """Registra una decisión tomada"""
    content = read_memory()
    if content is None:
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    # Buscar tabla de decisiones
    marker = "| Fecha | Decisión |"
    if marker in content:
        # Añadir a la tabla
        new_row = f"| {fecha} | {decision} | {contexto} | |\n"
        content = content.replace(marker, marker + new_row)
    else:
        # Crear tabla nueva
        decisions_section = """

## Decisiones Recientes

| Fecha | Decisión | Contexto | Referencia |
|-------|----------|----------|------------|
| {fecha} | {decision} | {contexto} | |

""".format(fecha=fecha, decision=decision, contexto=contexto)
        
        # Insertar antes de las notas
        if "## Notas" in content:
            content = content.replace("## Notas", decisions_section + "## Notas")
        else:
            content += decisions_section
    
    write_memory(content)
    return True

def add_error_solution(error, causa_raiz, solucion):
    """Registra un error y su solución"""
    content = read_memory()
    if content is None:
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    marker = "| [Pendiente] |"
    if marker in content:
        # Reemplazar placeholder con datos reales
        new_row = f"| {error} | {causa_raiz} | {solucion} | {fecha} |\n"
        content = content.replace(marker, new_row)
    else:
        # Añadir a la tabla de aprendizajes
        error_marker = "| Error | Causa Raíz |"
        if error_marker in content:
            new_row = f"| {error} | {causa_raiz} | {solucion} | {fecha} |\n"
            content = content.replace(error_marker, error_marker + new_row)
    
    write_memory(content)
    return True

def show_memory():
    """Muestra el contenido actual de memory.md"""
    content = read_memory()
    if content:
        print(content)
    else:
        print("[INFO] memory.md está vacío o no existe")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nComandos disponibles:")
        print("  add \"título\" \"descripción\"  - Añadir nuevo aprendizaje")
        print("  decision \"decisión\" \"contexto\" \"resultado\" - Registrar decisión")
        print("  error \"error\" \"causa\" \"solución\" - Registrar error y solución")
        print("  show                         - Mostrar memory.md actual")
        print("  update-fecha                 - Actualizar fecha de última modificación")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) >= 4:
        success = add_entry(sys.argv[2], sys.argv[3])
        sys.exit(0 if success else 1)
    
    elif command == "decision" and len(sys.argv) >= 5:
        success = add_decision(sys.argv[2], sys.argv[3], sys.argv[4])
        sys.exit(0 if success else 1)
    
    elif command == "error" and len(sys.argv) >= 5:
        success = add_error_solution(sys.argv[2], sys.argv[3], sys.argv[4])
        sys.exit(0 if success else 1)
    
    elif command == "show":
        show_memory()
        sys.exit(0)
    
    elif command == "update-fecha":
        success = update_fecha()
        sys.exit(0 if success else 1)
    
    else:
        print(f"[ERR] Comando desconocido o argumentos insuficientes: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()