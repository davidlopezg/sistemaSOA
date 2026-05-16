# systems-architecture.md - Reglas de Oro del Sistema

## Principios Fundamentales

### 1. Separación Cognición / Ejecución
- **Cognición:** `memory/`, `contexto/`, `agents/` - información y decisiones
- **Ejecución:** `technical_core/`, `systems/`, `generic/` - implementación
- **NUNCA mezclar:** Los datos de contexto no van en scripts de ejecución

### 2. Fragmentación de Tareas
- Prompts monolíticos PROHIBIDOS
- Todo se desglosa en unidades lógicas ejecutables (SDDs)
- Máximo 5 pasos por tarea antes de replantear

### 3. Ley de Pareto (80/20)
- Documentar solo el 20% de información que genera el 80% de decisiones
- Si un documento supera las 500 líneas, fragmentarlo

### 4. Nomenclatura Estricta
- Archivos/carpetas: **kebab-case** (`mi-archivo.md`, `modulo-test/`)
- SDDs: `SDD_XX_nombre.md`
- Variables: `snake_case`
- Constantes: `UPPER_SNAKE_CASE`
- Clases: `PascalCase`

### 5. Trazabilidad de Errores
- Todo error registrado debe indicar causa raíz
- Formato log: `[TIMESTAMP] [NIVEL] [COMPONENTE] [CAUSA] mensaje`
- Ejemplo: `[2026-05-16 10:30:00] [ERROR] [AuthModule] [TOKEN_EXPIRED] Token JWT expirado`

---

## Regla de Excepciones (SOLO proyectos técnicos)

### Formato Obligatorio

```python
# ✅ CORRECTO
try:
    resultado = operacion()
except SpecificException as e:
    logging.error(f"[CAUSA_RAÍZ] Descripción: {e}")
    # Explicación: Este error ocurre cuando X, hacer Y para resolver
    raise CustomException("Mensaje para usuario") from e

# ❌ PROHIBIDO
try:
    resultado = operacion()
except Exception:
    pass
```

### Categorías de Excepciones (Técnico)

| Categoría | Tratamiento | Ejemplo |
|-----------|-------------|---------|
| Validación | Log + return error | Datos malformados |
| Conexión | Log + reintentar | Timeout, DNS fail |
| Permiso | Log + throw | Auth fail, 403 |
| Sistema | Log + escalar | Disk full, OOM |

### Para Proyectos Genéricos
Usar sección "Problemas y Soluciones" en SDD en vez de try/except.

---

## Estructura de Entrega

### Pipeline de Validación

```
INPUT → CONTEXTO → PLAN → EJECUCIÓN → PRUEBAS → ENTREGA
         ↓          ↓         ↓           ↓
      Leer docs   SDD      Código      Arnés      /docs/
                 ↓         ↓        Checklists
              Módulos   Entregables
```

### Criterios de Entrega

Para que un output vaya a `/docs/` debe cumplir:
1. ✅ Código/entregable sin errores
2. ✅ Pasado por Arnés (técnico) o Checklists (genérico)
3. ✅ Documentado (comentarios inline + SDD actualizado)
4. ✅ Sin `TODO` o `FIXME` sin resolver
5. ✅ Excepciones tienen logging + causa raíz (técnico)

---

## Métricas de Salud del Sistema

| Métrica | Objetivo | Alarmas |
|---------|----------|---------|
| Tasa de errores | < 1% | > 5% |
| Tiempo de respuesta | < 5s | > 10s |
| Trazabilidad errores | 100% con causa | < 90% |

---

## Tipo de Proyecto

### Técnico
- Código, scripts, APIs, bases de datos
- Arnés de pruebas obligatorio
- Regla de excepciones obligatoria

### Genérico
- Marketing, docs, gestión, eventos
- Checklists en vez de tests
- "Problemas y Soluciones" en SDD

---

*Última actualización: 2026-05-16 v3.0*