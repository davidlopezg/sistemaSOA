# Sistema SOA - Sistema Multi-Agente

## Descripción

Infraestructura cognitiva auto-contenida para orquestar agentes IA con comandos estructurados, SDDs modulares y pipeline de validación. **Funciona para proyectos técnicos Y genéricos.**

## Estructura

```
sistemaSOA/
├── .agent/              # Configuración de comportamiento del agente
├── agente.md            # Orquestador - punto de entrada
├── memory/              # Cognición persistente
│   ├── memory.md        # Registro de aprendizajes y config del proyecto
│   └── conversaciones/  # Log de sesiones de trabajo
├── contexto/            # Reglas de negocio y specs
│   ├── systems-architecture.md  # Reglas de oro del sistema
│   ├── metas-objetivos.md      # KPIs y definición de éxito
│   └── knowledge.md            # Base de datos factual
├── agents/              # Sub-agentes especializados
├── systems/             # SDDs técnicos (proyectos de código)
├── manuals/             # Procedimientos operativos
├── technical_core/      # Para proyectos técnicos
│   ├── scripts/         # log_memory.py, log_conversation.py
│   └── arnes_tests/    # Validación automatizada
├── generic/             # Para proyectos NO técnicos
│   ├── sdds/            # SDDs genéricos
│   ├── checklists/      # Verificaciones manuales
│   └── scripts/         # log_progreso.py, log_decision.py
└── docs/                # Salida, plantillas y guías
```

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
| `/save` | Guardar sesión en memory/conversaciones/ |
| `/learn "texto"` | Guardar aprendizaje en memory/memory.md |
| `/help` | Mostrar todos los comandos disponibles |

## Primeros Pasos

### Clonar o instalar el repositorio

```bash
# Opción 1: Clonar el repositorio
git clone https://github.com/tu-usuario/SistemaSOA.git
cd SistemaSOA

# Opción 2: Si ya tienes el repositorio, navegar al directorio
cd ruta/a/SistemaSOA

# Opción 3: Copiar archivos manualmente si no usas git
cp -r SistemaSOA/ ~/tu-proyecto/
cd ~/tu-proyecto/
```

2. **Abrir sesión** con agente (Claude Code, OpenCode, etc.)
3. **Ejecutar `/initsoa`**
4. **Seleccionar tipo:** Técnico o Genérico
5. **Responder preguntas de contexto** (nombre, objetivo, stakeholders, etc.)
6. **Definir módulos** según el tipo

## Comportamiento del Sistema

### Proyectos Técnicos
- **SDD:** `docs/plantillas/SDD_TEMPLATE.md`
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