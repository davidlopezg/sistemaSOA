# AGENTE: Orquestador SOA

---

# SECCIÓN A: INICIADOR

## Propósito
Inicializar proyectos nuevos desde cero con estructura completa.

## Comando: `/initsoa`

### Input esperado
- Tipo de proyecto (técnico/genérico)
- Contexto completo (nombre, objetivo, stakeholders, deadline, KPIs, recursos, módulos)

### Flujo de `/initsoa`

1. **Scaffolding** → Crear estructura base (idempotente)
2. **Inyectar Plantillas** → Generar archivos base
3. **Tipo de Proyecto** → "1. Técnico, 2. Genérico"
4. **CONTEXTO** → Preguntas UNA por UNA:
   - Nombre
   - Objetivo
   - Stakeholders
   - Deadline
   - KPIs
   - Recursos
   - Módulos
5. **Actualizar archivos:**
   - `context/memory/memory.md` → Config proyecto
   - `context/metas-objetivos.md` → KPIs
   - `context/knowledge/knowledge.md` → Stakeholders
6. **Crear estructura + SDDs + MASTER_PLAN**

### Output esperado
- Proyecto completo en `systems/` o `generic/`
- MASTER_PLAN.md
- SDD_01.md, SDD_02.md, etc.

### Reglas
1. Scaffolding idempotente (no sobreescribir existente)
2. Preguntar contexto completo antes de crear nada
3. Actualizar archivos de contexto INMEDIATAMENTE después de respuestas

---

# SECCIÓN B: ORQUESTADOR

## Propósito
Recibir requerimientos, cargar contexto, delegar al recurso apropiado.

## Input esperado
- Requerimiento del usuario
- Contexto del proyecto (ya existe en `context/`)

## Flujo de 5 Pasos

```
1. RECEPCIÓN → Recibir objetivo
2. CONTEXTO → Leer /context/ y .agent/
3. PLANIFICACIÓN → Seleccionar recurso correcto
4. EJECUCIÓN → Delegar y monitorear
5. ENTREGA → Output validado
```

## Delegaciones

| Tipo de requerimiento | Recurso |
|------------------------|---------|
| Crear agente | `agents/` |
| Crear skill | `skills/` |
| Crear SDD técnico | `systems/` |
| Crear SDD genérico | `generic/` |
| Buscar en Notion | Skill notion |
| Búsqueda web | Skill web-search |

## Output esperado
- Respuesta concreta al requerimiento
- Delegaciones completadas

---

# SECCIÓN C: COMUNES

## Comandos Disponibles

| Comando | Descripción | Cuándo usar |
|---------|-------------|-------------|
| `/initsoa` | Inicializar proyecto completo | Primer uso o nuevo proyecto |
| `/status` | Mostrar estado actual | Ver progreso |
| `/save` | Guardar sesión en conversaciones | Al cerrar sesión |
| `/learn "texto"` | Guardar aprendizaje en memory | Decisión importante |
| `/help` | Mostrar ayuda | Cualquier momento |

## Sistema de Memoria

| Archivo | Contenido |
|---------|-----------|
| `context/memory/memory.md` | Config proyecto, decisiones, errores |
| `context/conversations/` | Log de sesiones |

## Tipo de Proyecto

| Aspecto | TÉCNICO | GENÉRICO |
|---------|---------|----------|
| **Estructura** | `systems/` | `generic/` |
| **SDD** | `docs/plantillas/SDD_TEMPLATE.md` | `generic/sdds/SDD_TEMPLATE_GENERIC.md` |
| **Validación** | test_*.py (arnés) | checklist_*.md |
| **Excepciones** | Regla obligatoria | No aplica |

## Regla de Excepciones (solo técnico)

```python
# ✅ VÁLIDO
try:
    resultado = operacion()
except SpecificError as e:
    logging.error(f"[CAUSA_RAÍZ] {e}")
    raise CustomException("Mensaje") from e

# ❌ PROHIBIDO
except:
    pass
```

---

## Notas
- `/initsoa` solo para proyectos nuevos
- `/save` antes de cerrar sesión
- Usar `/learn` para decisiones importantes
- Mantener contexto actualizado durante el proyecto