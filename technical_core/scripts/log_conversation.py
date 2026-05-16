#!/usr/bin/env python3
"""
log_conversation.py - Guardar transcript de sesiones

Este script crea un archivo de log con el transcript completo de
la conversación usuario-agente actual.

Uso:
    python log_conversation.py save [--resumen "texto"] [--usuario "nombre"]
    python log_conversation.py list [--limit N]
    python log_conversation.py show YYYY-MM-DD_HHmm
"""

import os
import sys
from datetime import datetime

CONVERSATIONS_DIR = "memory/conversaciones"
TEMPLATE_FILE = "memory/conversaciones/README.md"

def get_template():
    """Lee el template de conversación desde README.md"""
    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extraer solo el formato de log (desde "```markdown")
            start = content.find("```markdown")
            if start != -1:
                end = content.find("```", start + 10)
                return content[start + 10:end]
    except Exception as e:
        print(f"[WARN] No se pudo leer template: {e}", file=sys.stderr)
    
    # Template por defecto
    return """# Conversación: FECHA - RESUMEN

## Usuario
[Nombre]

## Inicio
[FECHA HORA]

## Tema
[Tema principal]

## Resumen
[Resumen de qué se hizo]

## Archivos Modificados
- [archivo1]
- [archivo2]

## Pendientes
- [Tarea 1]
- [Tarea 2]

## Fin
[FECHA HORA]

---
*Sesión guardada por agente*
"""

def generate_filename():
    """Genera nombre de archivo basado en fecha/hora"""
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H%M")
    return f"{fecha}_{hora}-sesion.md"

def save_conversation(resumen="Sesión sin título", usuario="Usuario"):
    """Guarda la conversación actual con timestamp"""
    # Crear directorio si no existe
    try:
        os.makedirs(CONVERSATIONS_DIR, exist_ok=True)
    except Exception as e:
        print(f"[ERR] No se pudo crear directorio: {e}", file=sys.stderr)
        return None
    
    filename = generate_filename()
    filepath = os.path.join(CONVERSATIONS_DIR, filename)
    
    now = datetime.now()
    fecha_hora = now.strftime("%Y-%m-%d %H:%M")
    
    template = get_template()
    
    content = f"""# Conversación: {now.strftime("%Y-%m-%d %H:%M")} - {resumen}

## Usuario
{usuario}

## Inicio
{fecha_hora}

## Tema
[Completar tras sesión]

## Resumen
[Resumen de qué se hizo]

## Archivos Modificados
[Listar archivos creados/modificados]

## Decisiones Tomadas
[Listar decisiones importantes]

## Pendientes
[Listar tareas pendientes]

## Fin
{fecha_hora}

---
*Guardado por: log_conversation.py*
"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Conversación guardada: {filepath}")
        return filepath
    except Exception as e:
        print(f"[ERR] Error guardando conversación: {e}", file=sys.stderr)
        return None

def list_conversations(limit=10):
    """Lista las últimas N conversaciones"""
    try:
        files = [f for f in os.listdir(CONVERSATIONS_DIR) 
                 if f.endswith('.md') and f != 'README.md']
        files.sort(reverse=True)
        
        print(f"[INFO] Últimas {min(limit, len(files))} conversaciones:\n")
        for f in files[:limit]:
            print(f"  📄 {f}")
        
        if len(files) > limit:
            print(f"\n  ... y {len(files) - limit} más")
    except FileNotFoundError:
        print("[INFO] No hay conversaciones guardadas")
    except Exception as e:
        print(f"[ERR] Error listando: {e}", file=sys.stderr)

def show_conversation(filename):
    """Muestra una conversación específica"""
    # Añadir extensión si no tiene
    if not filename.endswith('.md'):
        filename += '.md'
    
    filepath = os.path.join(CONVERSATIONS_DIR, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"[ERR] No encontrada: {filepath}")
    except Exception as e:
        print(f"[ERR] Error leyendo: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nComandos:")
        print("  save [--resumen 'texto']        - Guardar sesión actual")
        print("  list [--limit N]               - Listar conversaciones (default: 10)")
        print("  show YYYY-MM-DD_HHm             - Mostrar conversación específica")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "save":
        resumen = "Sesión sin título"
        usuario = "Usuario"
        
        # Parsear argumentos
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "--resumen" and i + 1 < len(sys.argv):
                resumen = sys.argv[i + 1]
                i += 2
            elif sys.argv[i] == "--usuario" and i + 1 < len(sys.argv):
                usuario = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        
        filepath = save_conversation(resumen, usuario)
        sys.exit(0 if filepath else 1)
    
    elif command == "list":
        limit = 10
        if len(sys.argv) > 2 and sys.argv[2] == "--limit":
            limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        
        list_conversations(limit)
        sys.exit(0)
    
    elif command == "show" and len(sys.argv) > 2:
        show_conversation(sys.argv[2])
        sys.exit(0)
    
    else:
        print(f"[ERR] Comando desconocido: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()