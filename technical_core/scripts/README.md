# scripts/ - Scripts de Automatización SOA

Este directorio contiene scripts de utilidad para automatizar tareas del sistema.

## Scripts Disponibles

| Script | Propósito | Uso |
|--------|-----------|-----|
| `log_memory.py` | Registrar aprendizajes en memory/memory.md | `python log_memory.py add "título" "descripción"` |
| `log_conversation.py` | Guardar sesión en conversaciones | `python log_conversation.py save --resumen "texto"` |

## log_memory.py

Registra aprendizajes importantes, decisiones y errores en `memory/memory.md`.

### Comandos

```bash
# Añadir aprendizaje
python technical_core/scripts/log_memory.py add "Título" "Descripción"

# Registrar decisión
python technical_core/scripts/log_memory.py decision "Decisión" "Contexto" "Resultado"

# Registrar error y solución
python technical_core/scripts/log_memory.py error "Error" "Causa raíz" "Solución"

# Mostrar memory actual
python technical_core/scripts/log_memory.py show

# Actualizar fecha
python technical_core/scripts/log_memory.py update-fecha
```

## log_conversation.py

Guarda el transcript de sesiones en `memory/conversaciones/`.

### Comandos

```bash
# Guardar sesión actual
python technical_core/scripts/log_conversation.py save --resumen "Resumen"

# Listar últimas conversaciones
python technical_core/scripts/log_conversation.py list --limit 5

# Mostrar conversación específica
python technical_core/scripts/log_conversation.py show 2026-05-16_1030
```

---

*Última actualización: 2026-05-16*