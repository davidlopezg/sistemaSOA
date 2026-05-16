#!/usr/bin/env python3
"""
test_exceptions.py - Valida regla de excepciones

Este script busca en el código Python bloques try/except vacíos
o sin logging, lo cual viola la regla inquebrantable del sistema.

Uso:
    python test_exceptions.py [directorio]
"""

import os
import re
import sys
from pathlib import Path

PATTERNS_BAD = [
    r'except\s*:\s*\n\s*pass\b',           # except: pass
    r'except\s+Exception\s*:\s*\n\s*pass\b',  # except Exception: pass
    r'except\s+\w+\s*:\s*\n\s*#.*pass',      # except Error: # pass (comentado)
]

PATTERNS_GOOD = [
    r'except.*logging\.',
    r'except.*log\.',
    r'except.*print\(',  # Aceptable si no hay mejor opción
]

def check_file(filepath):
    """Analiza un archivo Python buscando excepciones vacías."""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            for i, line in enumerate(lines, 1):
                # Skip comments
                stripped = line.strip()
                if stripped.startswith('#'):
                    continue
                    
                # Check for bad patterns
                for pattern in PATTERNS_BAD:
                    if re.search(pattern, content):
                        issues.append({
                            'file': filepath,
                            'line': i,
                            'issue': 'Excepción vacía o sin logging',
                            'match': re.search(pattern, content).group()
                        })
    except Exception as e:
        # Registro obligatorio - causa raíz: archivo no legible o encoding
        print(f"[ERR] No se pudo leer {filepath}: {e}", file=sys.stderr)
    
    return issues

def scan_directory(directory):
    """Escanea un directorio buscando archivos Python."""
    all_issues = []
    py_files = list(Path(directory).rglob('*.py'))
    
    for py_file in py_files:
        # Skip venv, __pycache__, node_modules
        skip_dirs = ['venv', '__pycache__', 'node_modules', '.git']
        if any(skip in str(py_file) for skip in skip_dirs):
            continue
            
        issues = check_file(py_file)
        all_issues.extend(issues)
    
    return all_issues

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"[INFO] Escaneando {target_dir} en busca de excepciones vacías...")
    
    issues = scan_directory(target_dir)
    
    if issues:
        print(f"\n[ERROR] Se encontraron {len(issues)} violaciones a la regla de excepciones:\n")
        for issue in issues:
            print(f"  📁 {issue['file']}:{issue['line']}")
            print(f"     └─ {issue['issue']}")
            print(f"     └─ Match: {issue['match']}\n")
        sys.exit(1)
    else:
        print("[OK] No se encontraron excepciones vacías. Regla cumplida.")
        sys.exit(0)

if __name__ == '__main__':
    main()