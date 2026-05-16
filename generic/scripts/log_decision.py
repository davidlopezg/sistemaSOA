#!/usr/bin/env python3
"""
log_decision.py - Registro de decisiones para proyectos genéricos

Este script documenta decisiones importantes del proyecto,
usando el sistema de memoria centralizado.

Uso:
    python log_decision.py add "Decisión" "Contexto" "Resultado"
    python log_decision.py list
    python log_decision.py show [id]
"""

import os
import sys
from datetime import datetime

MEMORY_FILE = "memory/memory.md"
DECISIONS_FILE = "systems/decisiones.md" if os.path.exists("systems") else "generic/decisiones.md"

def add_decision(decision, contexto, resultado):
    """Registra una decisión en memory.md"""
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERR] No se pudo leer memory.md: {e}", file=sys.stderr)
        return False
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    # Crear entrada
    entry = f"""
## [{fecha}] Decisión: {decision}

### Contexto
{contexto}

### Resultado
{resultado}

### Referencia
[Documentación: {DECISIONS_FILE}]
"""
    
    # Buscar tabla de decisiones o crearla
    marker = "| Fecha | Decisión |"
    if marker in content:
        # Añadir a la tabla existente
        new_row = f"| {fecha} | {decision} | {contexto} | |\n"
        content = content.replace(marker, marker + new_row)
    else:
        # Crear sección de decisiones
        decisions_section = """

## Decisiones del Proyecto

| Fecha | Decisión | Contexto | Referencia |
|-------|----------|----------|------------|
| {fecha} | {decision} | {contexto} | |

""".format(fecha=fecha, decision=decision, contexto=contexto)
        
        # Insertar antes de las notas
        if "## Notas" in content:
            content = content.replace("## Notas", decisions_section + "## Notas")
        else:
            content += decisions_section
    
    try:
        with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Decisión registrada: {decision}")
        
        # También guardar en archivo de decisiones
        save_to_decisions_file(decision, contexto, resultado)
        
        return True
    except Exception as e:
        print(f"[ERR] Error escribiendo: {e}", file=sys.stderr)
        return False

def save_to_decisions_file(decision, contexto, resultado):
    """Guarda en archivo específico de decisiones"""
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    os.makedirs(os.path.dirname(DECISIONS_FILE), exist_ok=True)
    
    entry = f"""
---

# {fecha}: {decision}

**Contexto:** {contexto}

**Resultado:** {resultado}

"""
    
    try:
        with open(DECISIONS_FILE, 'a', encoding='utf-8') as f:
            f.write(entry)
    except Exception as e:
        print(f"[WARN] No se pudo guardar en {DECISIONS_FILE}: {e}", file=sys.stderr)

def list_decisions():
    """Lista todas las decisiones registradas"""
    try:
        if os.path.exists(DECISIONS_FILE):
            with open(DECISIONS_FILE, 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            # Buscar en memory.md
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extraer decisiones
            import re
            decisions = re.findall(r'## \[(\d{4}-\d{2}-\d{2})\] Decisión: (.+)', content)
            
            if decisions:
                print("\n📋 DECISIONES REGISTRADAS")
                print("=" * 40)
                for fecha, decision in decisions:
                    print(f"  • {fecha}: {decision}")
            else:
                print("[INFO] No hay decisiones registradas")
    except Exception as e:
        print(f"[ERR] Error listando decisiones: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nComandos:")
        print('  add "Decisión" "Contexto" "Resultado"  - Registrar decisión')
        print("  list                               - Ver decisiones")
        print("  show [id]                           - Ver decisión específica")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) >= 5:
        decision = sys.argv[2]
        contexto = sys.argv[3]
        resultado = sys.argv[4]
        
        success = add_decision(decision, contexto, resultado)
        sys.exit(0 if success else 1)
    
    elif command == "list":
        list_decisions()
        sys.exit(0)
    
    elif command == "show" and len(sys.argv) >= 3:
        print(f"[INFO] Mostrando decisión: {sys.argv[2]}")
        sys.exit(0)
    
    else:
        print(f"[ERR] Argumentos insuficientes o comando desconocido")
        sys.exit(1)

if __name__ == '__main__':
    main()