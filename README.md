# Sistema SOA - Sistema Multi-Agente

[![Tests](https://github.com/tu-usuario/sistemaSOA/actions/workflows/tests.yml/badge.svg)](https://github.com/tu-usuario/sistemaSOA/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Descripción

Infraestructura cognitiva auto-contenida para orquestar agentes IA con comandos estructurados, SDDs modulares y pipeline de validación. **Funciona para proyectos técnicos Y genéricos.**

> 📚 **Documentación completa:** [Ver Guía Rápida](./docs/GUIA_RAPIDA.md)

## Estructura

```
sistemaSOA/
├── .agent/
│   └── SYSTEM_PROMPT_BACKUP.md  # Backup del prompt (deprecated)
│
├── agente.md            # Documentación del Orquestador (el prompt real está en .agent/)
│
├── agents/              # Plantillas de sub-agentes
│   ├── agent-builder.md # Plantilla para crear nuevos agentes
│   └── ejemplo-builder.md
│
├── skills/              # Plantillas de skills
│   └── skill-builder.md # Plantilla para crear nuevas skills
│
├── context/             # Contexto y cognición del proyecto
│   ├── conversations/   # Log de sesiones de trabajo
│   ├── memory/
│   │   └── memory.md    # Registro de aprendizajes y config del proyecto
│   ├── knowledge/       # Base de datos factual + documentos
│   │   └── knowledge.md
│   ├── metas-objetivos.md      # KPIs y definición de éxito
│   └── systems-architecture.md # Reglas de oro del sistema
│
├── systems/             # SDDs técnicos (proyectos de código)
│   ├── MASTER_PLAN.md
│   └── SDD_01_*.md
│
├── generic/             # Para proyectos NO técnicos
│   ├── sdds/            # SDDs genéricos
│   └── checklists/      # Verificaciones manuales
│
├── technical_core/      # Para proyectos técnicos
│   ├── scripts/         # log_memory.py, log_conversation.py
│   └── arnes_tests/     # Validación automatizada
│
├── manuals/             # Procedimientos operativos
└── docs/                # Salida, plantillas y guías
```

## Propósito de cada directorio

| Directorio | Propósito |
|------------|-----------|
| `.agent/` | Configuración del comportamiento del agente |
| `agente.md` | Orquestador: inicia proyectos y delega tareas |
| `agents/` | Plantillas para crear sub-agentes especializados |
| `skills/` | Plantillas para crear skills (capacidades externas) |
| `context/` | Todo el contexto del proyecto activo |
| `context/memory/` | Aprendizajes, decisiones, config persistente |
| `context/conversations/` | Historial de sesiones |
| `context/knowledge/` | Datos factuales y documentos de referencia |
| `context/metas-objetivos.md` | KPIs, hitos, criterios de éxito |
| `context/systems-architecture.md` | Reglas de oro del sistema |
| `systems/` | SDDs para proyectos técnicos (código) |
| `generic/` | SDDs para proyectos genéricos (marketing, docs, gestión) |
| `technical_core/` | Scripts y tests para proyectos técnicos |
| `manuals/` | Procedimientos operativos y guías |
| `docs/` | Plantillas, guías rápidas, salida de trabajo |

## Tipo de Proyectos Soportados

### Técnico
- Desarrollo de software
- Scripts y automatización
- APIs, bases de datos

### Genérico
- Marketing y campañas
- Documentación
- Gestión de proyectos
- Formación
- Eventos
- Consultoría

## Comandos Disponibles

| Comando | Descripción |
|----------|-------------|
| `/initsoa` | Inicializar proyecto (selector: técnico/genérico + contexto) |
| `/status` | Ver estado actual del proyecto |
| `/save` | Guardar sesión en context/conversations/ |
| `/learn "texto"` | Guardar aprendizaje en context/memory/memory.md |
| `/help` | Mostrar todos los comandos disponibles |

## Primeros Pasos

1. **Clonar o instalar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/sistemaSOA.git
   cd sistemaSOA
   ```

2. **Abrir sesión** con agente (Claude Code, OpenCode, etc.)

3. **Ejecutar `/initsoa`**

4. **Seleccionar tipo:** Técnico o Genérico

5. **Responder preguntas de contexto** (nombre, objetivo, stakeholders, etc.)

6. **Definir módulos** según el tipo

## Comportamiento del Sistema

### Proyectos Técnicos
- **SDD:** `systems/sdds/SDD_TEMPLATE.md`
- **Validación:** Arnés de pruebas (`technical_core/arnes_tests/`)
- **Scripts:** `log_memory.py`, `log_conversation.py`
- **Regla de excepciones:** Obligatoria

### Proyectos Genéricos
- **SDD:** `generic/sdds/SDD_TEMPLATE_GENERIC.md`
- **Validación:** Checklists (`generic/checklists/`)
- **Scripts:** `log_progreso.py`, `log_decision.py`
- **Problemas/Soluciones:** Documentados en SDD

## Flujo de `/initsoa`

```
1. Scaffolding base
2. Inyectar plantillas
3. Preguntar tipo (técnico/genérico)
4. Preguntar CONTEXTO:
   - Nombre del proyecto
   - Objetivo principal
   - Stakeholders
   - Deadline
   - KPIs de éxito
   - Recursos disponibles
   - Módulos/SDDs
5. ACTUALIZAR archivos de contexto
6. Crear estructura + SDDs + MASTER_PLAN
```

## Scripts Disponibles

### Técnico
```bash
python technical_core/scripts/log_memory.py add "Título" "Descripción"
python technical_core/scripts/log_memory.py decision "Decisión" "Contexto" "Resultado"
python technical_core/scripts/log_conversation.py save --resumen "Resumen"
```

### Genérico
```bash
python generic/scripts/log_progreso.py fase "Nombre fase" --completo 75
python generic/scripts/log_progreso.py hito "Nombre hito" --completado
python generic/scripts/log_decision.py add "Decisión" "Contexto" "Resultado"
python generic/scripts/log_progreso.py show
```

---

*SOA v3.0 - Structured Orchestration Architecture*