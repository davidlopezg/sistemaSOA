# generic/ - Proyectos No Técnicos

Esta carpeta contiene la estructura para proyectos que no son de desarrollo de software.

## Estructura

```
generic/
├── sdds/                    # System Design Documents genéricos
│   ├── SDD_TEMPLATE_GENERIC.md    # Plantilla SDD
│   └── _hitos.md                  # Registro de hitos (generado)
├── checklists/              # Verificaciones manuales
│   ├── checklist_entrega.md        # Verificación antes de entrega
│   └── checklist_calidad.md       # Control de calidad
└── scripts/                 # Scripts de automatización
    ├── log_progreso.py            # Registrar progreso
    └── log_decision.py            # Registrar decisiones
```

## Tipos de Proyecto

- Marketing y campañas
- Documentación
- Gestión de proyectos
- Formación
- Eventos
- Consultoría

## Uso

### Durante `/initsoa`
Al seleccionar tipo "Genérico", el sistema:
1. Crea estructura `generic/sdds/`, `generic/checklists/`, `generic/scripts/`
2. Genera SDDs usando `SDD_TEMPLATE_GENERIC.md`
3. Usa checklists en vez de tests automatizados

### Durante el trabajo
1. Leer SDD del módulo
2. Ejecutar tareas
3. Validar con checklists
4. Actualizar progreso con scripts

### Scripts disponibles

```bash
# Registrar progreso de fase
python generic/scripts/log_progreso.py fase "Nombre fase" --completo 75 --nota "Notas"

# Registrar hito completado
python generic/scripts/log_progreso.py hito "Nombre hito" --completado

# Ver estado del proyecto
python generic/scripts/log_progreso.py show

# Registrar decisión
python generic/scripts/log_decision.py add "Decisión" "Contexto" "Resultado"
```

---

*Última actualización: 2026-05-16*