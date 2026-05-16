# GUÍA RÁPIDA - Sistema SOA

Infraestructura cognitiva para orquestar agentes IA. Funciona para proyectos técnicos Y genéricos.

---

## FLUJO COMPLETO v3.0

```
/initsoa → Tipo → CONTEXTO → Módulos → SDDs → Trabajar → Entregar → Cerrar
           │       │
           │       └── ¿Nombre? ¿Objetivo? ¿Stakeholders? ¿Deadline?
           │           ¿KPIs? ¿Recursos?
           │
           └── ¿Técnico o Genérico?
```

---

## PASO 1: INICIALIZAR (/initsoa v3.0)

```bash
# Clonar y ejecutar
git clone https://tu-repo/sistemaSOA.git mi-proyecto
cd mi-proyecto
/initsoa
```

### El agente preguntará:

**1. Tipo de proyecto:**
```
¿Qué tipo de proyecto necesitas?
  [1] Técnico (código, scripts)
  [2] Genérico (marketing, docs, gestión)
```

**2. CONTEXTO del proyecto:**
```
¿Cómo se llama el proyecto? → [Nombre]
¿Cuál es el objetivo principal? → [Objetivo]
¿Quiénes son los stakeholders? → [Lista]
¿Hay fecha límite? → [Fecha]
¿Cómo medimos el éxito? → [KPIs]
¿Qué herramientas tienes? → [Recursos]
¿Módulos/SDDs? → [Lista]
```

**3. Módulos:**
```
¿Cuántos módulos necesitas?
Ejemplo: "3 módulos: auth, API, docs"
```

### El agente actualiza:

| Archivo | Contenido |
|---------|-----------|
| `memory/memory.md` | Config: nombre, tipo, objetivo, deadline |
| `contexto/metas-objetivos.md` | KPIs, hitos, criterios de éxito |
| `contexto/knowledge.md` | Stakeholders, recursos, negocio |

Y genera:
- `MASTER_PLAN.md`
- `SDD_01_nombre.md`, `SDD_02_nombre.md`, etc.

---

## PASO 2: TRABAJAR EN MÓDULOS

### Si es TÉCNICO:

```
1. Leer SDD del módulo
2. Implementar código
3. VALIDAR con arnés:
   python technical_core/arnes_tests/test_estructura.py .
   python technical_core/arnes_tests/test_nomenclatura.py .
   python technical_core/arnes_tests/test_exceptions.py .
4. Si pasa → Entregar a /docs/
5. REGISTRAR: /learn "Módulo X completado"
```

### Si es GENÉRICO:

```
1. Leer SDD del módulo
2. Ejecutar tareas
3. VALIDAR con checklists:
   - generic/checklists/checklist_entrega.md
   - generic/checklists/checklist_calidad.md
4. Si pasa → Entregar
5. REGISTRAR:
   python generic/scripts/log_progreso.py fase "Nombre" --completo 75
```

---

## PASO 3: CERRAR SESIÓN

```bash
# Guardar conversación (sesiones largas o importantes)
/save

# Guardar aprendizaje (decisiones, errores, preferencias)
/learn "Decisión importante tomada"
```

---

## COMANDOS PRINCIPALES

| Comando | Función | Cuándo |
|---------|---------|--------|
| `/initsoa` | Inicializar proyecto (v3.0 - con contexto) | Primer uso |
| `/status` | Ver estado | Siempre |
| `/save` | Guardar sesión | Cierre |
| `/learn "texto"` | Guardar aprendizaje | Decisiones |
| `/help` | Mostrar ayuda | Siempre |

---

## COMPARACIÓN: TÉCNICO vs GENÉRICO

| Aspecto | TÉCNICO | GENÉRICO |
|---------|---------|----------|
| **Ejemplos** | API, scripts, web | Marketing, docs, gestión |
| **Estructura** | `systems/` | `generic/` |
| **SDD** | docs/plantillas/SDD_TEMPLATE.md | generic/sdds/SDD_TEMPLATE_GENERIC.md |
| **Validación** | Tests automatizados (arnés) | Checklists manuales |
| **Scripts** | log_memory.py, log_conversation.py | log_progreso.py, log_decision.py |
| **Excepciones** | Regla obligatoria | No aplica |

---

## REGLA DE EXCEPCIONES (SOLO TÉCNICO)

```python
# ❌ PROHIBIDO
try:
    operacion()
except:
    pass

# ✅ OBLIGATORIO
try:
    operacion()
except SpecificError as e:
    logging.error(f"[CAUSA_RAÍZ] Descripción: {e}")
    # Explicación: Este error ocurre cuando X
    raise CustomException("Mensaje") from e
```

---

## ESTRUCTURA DE CARPETAS

```
sistemaSOA/
├── .agent/              # Comportamiento del agente
├── agente.md            # Orquestador
├── memory/              # Memoria
│   ├── memory.md        # → Config proyecto + aprendizajes
│   └── conversaciones/  # → Log sesiones
├── contexto/            # Reglas y specs
│   ├── metas-objetivos.md  # → KPIs, hitos, éxito
│   └── knowledge.md     # → Stakeholders, recursos, negocio
├── agents/              # Sub-agentes
├── systems/             # SDDs técnicos
├── manuals/             # Procedimientos
├── technical_core/      # Para proyectos técnicos
│   ├── scripts/         # log_memory.py, log_conversation.py
│   └── arnes_tests/     # Tests automatizados
└── generic/             # Para proyectos genéricos
    ├── sdds/            # SDDs genéricos
    ├── checklists/      # Verificaciones manuales
    └── scripts/         # log_progreso.py, log_decision.py
```

---

## SCRIPTS DISPONIBLES

### Técnico
```bash
# Registrar aprendizaje
python technical_core/scripts/log_memory.py add "Título" "Descripción"

# Registrar decisión
python technical_core/scripts/log_memory.py decision "Decisión" "Contexto" "Resultado"

# Guardar sesión
python technical_core/scripts/log_conversation.py save --resumen "Resumen"
```

### Genérico
```bash
# Registrar progreso de fase
python generic/scripts/log_progreso.py fase "Nombre fase" --completo 75 --nota "Notas"

# Registrar hito
python generic/scripts/log_progreso.py hito "Nombre hito" --completado

# Registrar decisión
python generic/scripts/log_decision.py add "Decisión" "Contexto" "Resultado"

# Ver estado
python generic/scripts/log_progreso.py show
```

---

## FLUJO DE CONTEXTO (v3.0)

```
Respuestas del usuario en /initsoa
       │
       ▼
┌─────────────────────────────────────┐
│  memory/memory.md                   │
│  └── Config proyecto completo      │
├─────────────────────────────────────┤
│  contexto/metas-objetivos.md       │
│  └── KPIs, hitos, éxito            │
├─────────────────────────────────────┤
│  contexto/nowledge.md              │
│  └── Stakeholders, recursos        │
└─────────────────────────────────────┘
       │
       ▼
  SDDs incluyen contexto del proyecto
```

---

## CHECKLIST DE ENTREGA

### Técnico
- [ ] Código compila sin errores
- [ ] Arnés pasa 100%
- [ ] Sin excepciones vacías
- [ ] SDD actualizado
- [ ] Contexto actualizado

### Genérico
- [ ] Todos los entregables presentes
- [ ] Checklist entrega marcado
- [ ] Checklist calidad marcado
- [ ] SDD actualizado
- [ ] Contexto actualizado

---

## Nomenclatura

- Archivos: `kebab-case` (`mi-archivo.md`)
- SDDs: `SDD_01_nombre.md`
- Conversaciones: `YYYY-MM-DD_HHmm-resumen.md`

---

*SOA v3.0 - Con contexto completo del proyecto*