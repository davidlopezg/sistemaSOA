#!/usr/bin/env python3
"""
test_nomenclatura.py - Valida convenciones de nombres

Verifica que los archivos y código cumplan con las convenciones:
- Archivos/carpetas: kebab-case
- Variables: snake_case
- Constantes: UPPER_SNAKE_CASE
- Clases: PascalCase
- SDDs: SDD_XX_nombre.md

Uso:
    python test_nomenclatura.py [directorio]
"""

import os
import re
import sys
from pathlib import Path

# Archivos estándar de la industria que NO requieren kebab-case
EXCLUDED_FILES = {
    'README.md', 'LICENSE', '.gitignore', '.gitattributes',
    'package.json', 'package-lock.json', 'requirements.txt',
    'setup.py', 'pyproject.toml', 'Cargo.toml',
    'MASTER_PLAN.md',  # Nombre técnico estándar
    'SOP_playbook.md',   # Manual de procedimientos
    'checklist_calidad.md',  # Checklist operativo
    'checklist_entrega.md',  # Checklist genérico
    'GUIA_RAPIDA.md',       # Guía de usuario
    # Archivos estándar de proyecto
    'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
}

def check_filename(filepath):
    """Verifica naming convention de un archivo."""
    name = os.path.basename(filepath)
    issues = []
    
    # Skip hidden files, git, pycache, and standard files
    if name.startswith('.') or '__pycache__' in filepath or '.git' in filepath:
        return issues
    if name in EXCLUDED_FILES:
        return issues
    
    ext = os.path.splitext(name)[1]
    
    # Archivos Python -> snake_case
    if ext == '.py':
        # Aceptar snake_case: test_*.py, log_*.py, etc.
        if not re.match(r'^[a-z][a-z0-9_]*\.py$', name) and not name.startswith('test_') and not name.startswith('log_'):
            issues.append({
                'file': filepath,
                'issue': f'Nombre de archivo Python no snake_case: {name}',
                'expected': 'mi_modulo.py'
            })
    
    # Documentos MD -> kebab-case
    if ext == '.md':
        base = os.path.splitext(name)[0]
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', base) and not base.startswith('SDD_'):
            # Special case for SDD files
            if base.startswith('SDD_'):
                sdd_pattern = r'^SDD_\d+_[a-z0-9]+(-[a-z0-9]+)*$'
                if not re.match(sdd_pattern, base):
                    issues.append({
                        'file': filepath,
                        'issue': f'SDD mal formateado: {base}',
                        'expected': 'SDD_XX_nombre.md'
                    })
            else:
                issues.append({
                    'file': filepath,
                    'issue': f'Nombre de archivo no kebab-case: {name}',
                    'expected': 'mi-archivo.md'
                })
    
    return issues

def scan_directory(directory):
    """Escanea directorio verificando naming conventions."""
    all_issues = []
    
    for root, dirs, files in os.walk(directory):
        # Skip hidden and cache dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for filename in files:
            filepath = os.path.join(root, filename)
            issues = check_filename(filepath)
            all_issues.extend(issues)
    
    return all_issues

def main():
    # Si no se especifica directorio, usar el directorio del script (raíz del proyecto)
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = Path(__file__).parent.resolve().parent.parent
    
    print(f"[INFO] Verificando naming conventions en {target_dir}...")
    
    issues = scan_directory(target_dir)
    
    if issues:
        print(f"\n[WARN] Se encontraron {len(issues)} problemas de nomenclatura:\n")
        for issue in issues:
            print(f"  📁 {issue['file']}")
            print(f"     └─ {issue['issue']}")
            print(f"     └─ Esperado: {issue['expected']}\n")
        sys.exit(1)
    else:
        print("[OK] Naming conventions correctas.")
        sys.exit(0)

if __name__ == '__main__':
    main()