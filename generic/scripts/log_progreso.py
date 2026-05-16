#!/usr/bin/env python3
"""
log_progreso.py - Registro de progreso para proyectos genéricos

Este script actualiza memory.md y los SDDs con el progreso
para proyectos no técnicos.

Uso:
    python log_progreso.py fase "Nombre fase" --completo 75 --nota "texto"
    python log_progreso.py hito "Nombre hito" --completado
    python log_progreso.py show
"""

import os
import sys
from datetime import datetime

MEMORY_FILE = "memory/memory.md"
SDDS_DIR = "generic/sdds"

def update_memory_progreso(fase, porcentaje, nota=""):
    """Actualiza memory.md con progreso de proyecto"""
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERR] No se pudo leer memory.md: {e}", file=sys.stderr)
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    # Buscar sección de notas o crear antes de la última actualización
    marker = "*Última actualización:"
    progreso_entry = f"""
## [{fecha}] Progreso: {fase}

- **Porcentaje:** {porcentaje}%
- **Nota:** {nota if nota else "[Sin notas]"}
"""
    
    if marker in content:
        parts = content.split(marker)
        new_content = parts[0] + progreso_entry + "\n" + marker + parts[1]
    else:
        new_content = content + progreso_entry
    
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] Progreso registrado: {fase} - {porcentaje}%")
        return True
    except Exception as e:
        print(f"[ERR] Error escribiendo: {e}", file=sys.stderr)
        return False

def register_hito(hito_nombre, completado=False):
    """Registra un hito en un archivo de hitos"""
    fecha = datetime.now().strftime("%Y-%m-%d")
    estado = "✅ Completado" if completado else "⏳ Pendiente"
    
    entry = f"""
## [{fecha}] Hito: {hito_nombre}

- **Estado:** {estado}
- **Detalles:** [Descripción]

---
"""
    
    # Guardar en archivo de hitos
    os.makedirs(SDDS_DIR, exist_ok=True)
    hitos_file = os.path.join(SDDS_DIR, "_hitos.md")
    
    try:
        with open(hitos_file, 'a', encoding='utf-8') as f:
            f.write(entry)
        print(f"[OK] Hito registrado: {hito_nombre} ({estado})")
        return True
    except Exception as e:
        print(f"[ERR] Error registrando hito: {e}", file=sys.stderr)
        return False

def show_status():
    """Muestra estado actual del proyecto desde memory.md"""
    print("\n📊 ESTADO DEL PROYECTO")
    print("=" * 40)
    
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraer estado (buscar sin negritas)
        import re
        
        # Estado del proyecto
        estado_match = re.search(r'Estado del Proyecto:\s*(.+)', content)
        if estado_match:
            print(f"Estado: {estado_match.group(1).strip()}")
        
        # Progreso
        progresos = re.findall(r'## \[(\d{4}-\d{2}-\d{2})\] Progreso: (.+)', content)
        if progresos:
            print("\nÚltimos progresos:")
            for fecha, fase in progresos[-5:]:
                pct_match = re.search(r'(\d+)%', fase)
                pct = pct_match.group(1) if pct_match else "?"
                print(f"  • {fecha}: {fase.split('-')[0].strip()} ({pct}%)")
        else:
            print("\nSin progresos registrados")
        
        # Config del proyecto
        print("\nConfiguración:")
        nombre_match = re.search(r'nombre:\s*(.+)', content)
        tipo_match = re.search(r'tipo:\s*(.+)', content)
        deadline_match = re.search(r'deadline:\s*(.+)', content)
        
        if nombre_match:
            print(f"  Nombre: {nombre_match.group(1).strip()}")
        if tipo_match:
            print(f"  Tipo: {tipo_match.group(1).strip()}")
        if deadline_match:
            print(f"  Deadline: {deadline_match.group(1).strip()}")
        
    except FileNotFoundError:
        print("[INFO] Ejecutar /initsoa primero")
    except Exception as e:
        print(f"[ERR] Error leyendo estado: {e}", file=sys.stderr)
    
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nComandos:")
        print('  fase "Nombre" --completo N --nota "texto"  - Registrar progreso')
        print("  hito \"Nombre\" --completado                  - Registrar hito")
        print("  show                                      - Ver estado")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "fase" and len(sys.argv) >= 3:
        fase_nombre = sys.argv[2]
        porcentaje = 50
        nota = ""
        
        # Parsear argumentos
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--completo" and i + 1 < len(sys.argv):
                porcentaje = int(sys.argv[i + 1])
                i += 2
            elif sys.argv[i] == "--nota" and i + 1 < len(sys.argv):
                nota = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        
        success = update_memory_progreso(fase_nombre, porcentaje, nota)
        sys.exit(0 if success else 1)
    
    elif command == "hito" and len(sys.argv) >= 3:
        hito = sys.argv[2]
        completado = "--completado" in sys.argv
        
        success = register_hito(hito, completado)
        sys.exit(0 if success else 1)
    
    elif command == "show":
        show_status()
        sys.exit(0)
    
    else:
        print(f"[ERR] Comando desconocido: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()