#!/usr/bin/env python3
"""
test_estructura.py - Valida estructura de carpetas SOA

Verifica que la estructura de directorios cumpla con la topología definida:
- .agent/
- agente.md
- memory/
- contexto/
- agents/
- systems/
- manuals/
- technical_core/
- docs/

Uso:
    python test_estructura.py [directorio]
"""

import os
import sys
from pathlib import Path

REQUIRED_STRUCTURE = {
    'directories': [
        '.agent',
        'memory/conversaciones',
        'contexto',
        'agents',
        'systems',
        'manuals',
        'technical_core/skills',
        'technical_core/arnes_tests/data',
        'technical_core/logs',
        'docs/plantillas',
    ],
    'files': [
        'agente.md',
        'README.md',
        '.agent/SYSTEM_PROMPT.md',
        'docs/plantillas/SDD_TEMPLATE.md',
        'contexto/systems-architecture.md',
        'contexto/metas-objetivos.md',
        'memory/memory.md',
        'manuals/SOP_playbook.md',
        'manuals/checklist_calidad.md',
    ]
}

def check_structure(base_dir):
    """Verifica la estructura de directorios y archivos."""
    missing = {'dirs': [], 'files': []}
    
    # Check directories
    for dir_path in REQUIRED_STRUCTURE['directories']:
        full_path = os.path.join(base_dir, dir_path)
        if not os.path.isdir(full_path):
            missing['dirs'].append(dir_path)
    
    # Check files
    for file_path in REQUIRED_STRUCTURE['files']:
        full_path = os.path.join(base_dir, file_path)
        if not os.path.isfile(full_path):
            missing['files'].append(file_path)
    
    return missing

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"[INFO] Verificando estructura SOA en {target_dir}...")
    
    missing = check_structure(target_dir)
    
    if missing['dirs'] or missing['files']:
        if missing['dirs']:
            print(f"\n[ERROR] Directorios faltantes ({len(missing['dirs'])}):")
            for d in missing['dirs']:
                print(f"  📁 {d}")
        
        if missing['files']:
            print(f"\n[ERROR] Archivos faltantes ({len(missing['files'])}):")
            for f in missing['files']:
                print(f"  📄 {f}")
        
        print("\n[INFO] Ejecutar /initsoa para crear estructura completa")
        sys.exit(1)
    else:
        print("[OK] Estructura SOA completa y válida.")
        sys.exit(0)

if __name__ == '__main__':
    main()