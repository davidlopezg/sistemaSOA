# SOP_playbook.md - Procedimientos Operativos Estándar

## Índice

1. [Protocolo `/initsoa`](#protocolo-initsoa)
2. [Protocolo de Trabajo](#protocolo-de-trabajo)
3. [Protocolo de Validación](#protocolo-de-validación)
4. [Protocolo de Cierre de Sesión](#protocolo-de-cierre-de-sesión)
5. [Checklist de Entrega](#checklist-de-entrega)

---

## Protocolo `/initsoa`

**Versión:** 3.0  
**Cuándo:** Primera vez o nuevo proyecto

### Pasos (ejecutar SIN pedir permiso)

```
┌─────────────────────────────────────────────────────────────┐
│  1. Scaffolding Base                                        │
│     Crear estructura de carpetas (idempotente)               │
│     ├── .agent/                                             │
│     ├── agente.md                                           │
│     ├── memory/memory.md                                    │
│     ├── memory/conversaciones/                              │
│     ├── contexto/                                           │
│     ├── agents/                                             │
│     ├── manuals/                                            │
│     └── docs/plantillas/                                    │
├─────────────────────────────────────────────────────────────┤
│  2. Inyectar Plantillas                                     │
│     Generar si no existen:                                  │
│     ├── docs/plantillas/SDD_TEMPLATE.md                    │
│     ├── contexto/systems-architecture.md                   │
│     ├── contexto/metas-objetivos.md                         │
│     ├── contexto/knowledge.md                               │
│     └── memory/conversaciones/README.md                     │
├─────────────────────────────────────────────────────────────┤
│  3. Preguntar Tipo                                          │
│                                                             │
│     > "¿Qué tipo de proyecto necesitas?"                    │
│     > [1] Técnico (código, scripts, desarrollo)             │
│     > [2] Genérico (marketing, docs, gestión)               │
├─────────────────────────────────────────────────────────────┤
│  4. Preguntas de CONTEXTO (UNA por UNA)                     │
│                                                             │
│     1. Nombre del proyecto                                 │
│     2. Objetivo principal                                   │
│     3. Stakeholders (nombres y roles)                       │
│     4. Deadline (YYYY-MM-DD)                                │
│     5. KPIs de éxito (métricas concretas)                    │
│     6. Recursos/herramientas disponibles                    │
│     7. Módulos/SDDs (cuántos y cuáles)                      │
├─────────────────────────────────────────────────────────────┤
│  5. Actualizar Archivos de Contexto                         │
│                                                             │
│     | Pregunta        | Guarda en                          | │
│     |-----------------|------------------------------------| │
│     | Nombre, Tipo    | memory/memory.md                  | │
│     | Objetivo, KPIs   | contexto/metas-objetivos.md      | │
│     | Stakeholders    | contexto/knowledge.md             | │
│     | Recursos        | contexto/knowledge.md             | │
│     | Deadline        | Ambos                             | │
├─────────────────────────────────────────────────────────────┤
│  6. Crear Estructura Específica                             │
│                                                             │
│     Técnico → systems/, technical_core/                     │
│     Genérico → generic/                                     │
├─────────────────────────────────────────────────────────────┤
│  7. Generar SDDs + MASTER_PLAN                               │
│                                                             │
│     ├── MASTER_PLAN.md                                     │
│     ├── SDD_01_nombre.md                                   │
│     ├── SDD_02_nombre.md                                   │
│     └── ...                                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Protocolo de Trabajo

### Proyecto TÉCNICO

```
1. LEER SDD del módulo
   └── Entender qué debe hacer

2. IMPLEMENTAR código
   └── Regla: todo except con logging + causa raíz

3. VALIDAR con arnés
   python technical_core/arnes_tests/test_estructura.py .
   python technical_core/arnes_tests/test_nomenclatura.py .
   python technical_core/arnes_tests/test_exceptions.py .
   
   ⚠️ Si falla → Corregir → Repetir paso 3

4. ENTREGAR
   └── Output validado va a /docs/

5. REGISTRAR
   └── /learn "Módulo X completado con decisión Y"
```

### Proyecto GENÉRICO

```
1. LEER SDD del módulo
   └── Entender qué debe hacer

2. EJECUTAR tareas
   └── Seguir fases del plan de trabajo

3. VALIDAR con checklists
   ├── generic/checklists/checklist_entrega.md
   └── generic/checklists/checklist_calidad.md
   
   ⚠️ Si incompleto → Completar → Repetir paso 3

4. ENTREGAR
   └── Output validado

5. REGISTRAR
   ├── python generic/scripts/log_progreso.py fase "Nombre" --completo 75
   └── /learn "Fase X completada"
```

---

## Protocolo de Validación

### Técnico (Arnés Automatizado)

```bash
# Validar estructura del proyecto
python technical_core/arnes_tests/test_estructura.py .

# Validar naming conventions
python technical_core/arnes_tests/test_nomenclatura.py .

# Validar regla de excepciones
python technical_core/arnes_tests/test_exceptions.py .
```

**Resultado esperado:** `[OK]` para todos

### Genérico (Checklists Manuales)

```bash
# Verificar entrega
1. Abrir generic/checklists/checklist_entrega.md
2. Marcar TODOS los items

# Verificar calidad
1. Abrir generic/checklists/checklist_calidad.md
2. Marcar TODOS los items
```

**Resultado esperado:** 100% de items marcados

---

## Protocolo de Cierre de Sesión

### Cuándo guardar en `memory/conversaciones/`

- Sesiones largas (> 30 minutos)
- Sesiones con decisiones importantes
- Cuando el usuario lo pida con `/save`

```bash
# Guardar conversación
python technical_core/scripts/log_conversation.py save --resumen "Resumen de sesión"

# O usar comando
/save
```

### Cuándo guardar en `memory/memory.md`

- Decisiones de arquitectura/proyecto
- Errores y soluciones descubiertas
- Cambios de estado del proyecto
- Preferencias del usuario

```bash
# Registrar aprendizaje
python technical_core/scripts/log_memory.py add "Título" "Descripción"

# Registrar decisión
python technical_core/scripts/log_memory.py decision "Decisión" "Contexto" "Resultado"

# O usar comando
/learn "Mensaje importante"
```

---

## Checklist de Entrega

### Técnico

- [ ] Código compila/ejecuta sin errores
- [ ] Arnés de pruebas pasa (100%)
- [ ] Sin excepciones vacías
- [ ] Todo `except` tiene logging + causa raíz
- [ ] SDD actualizado (estado: Validado)
- [ ] Contexto actualizado (metas-objetivos, knowledge)

### Genérico

- [ ] Todos los entregables presentes
- [ ] Checklist entrega completado (100%)
- [ ] Checklist calidad completado (100%)
- [ ] Decisiones documentadas
- [ ] SDD actualizado (estado: Completado)
- [ ] Contexto actualizado (metas-objetivos, knowledge)

---

## Referencias

| Recurso | Ubicación |
|---------|-----------|
| Plantilla SDD Técnico | `docs/plantillas/SDD_TEMPLATE.md` |
| Plantilla SDD Genérico | `generic/sdds/SDD_TEMPLATE_GENERIC.md` |
| Guía Rápida | `docs/GUIA_RAPIDA.md` |
| Reglas del Sistema | `contexto/systems-architecture.md` |
| Definición de Éxito | `contexto/metas-objetivos.md` |

---

*Última actualización: 2026-05-16 v3.0*