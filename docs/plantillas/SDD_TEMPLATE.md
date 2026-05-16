# SDD_TEMPLATE.md - System Design Document

Plantilla para documentar módulos técnicos del sistema SOA.

---

## 1. Alcance

**ID:** SDD_XX  
**Nombre:** [Nombre del módulo]  
**Versión:** 1.0  
**Estado:** [Borrador | En desarrollo | Validado | Producción]  
**Fecha:** YYYY-MM-DD

### Descripción
[Descripción clara del propósito y alcance de este módulo]

### Dependencias
- `SDD_XX_nombre.md` (si aplica)
- Librería/dependencia X (versión)

### Responsabilidades
- [Responsabilidad 1]
- [Responsabilidad 2]

---

## 2. Estructura de Datos

### Entidades Principales

```yaml
entidad_principal:
  campos:
    - nombre: string
      tipo: string
      descripcion: string
      requerido: boolean
    - nombre: string
      tipo: number
      descripcion: string
      requerido: boolean
  relaciones:
    - entidad: entidad_relacionada
      tipo: uno-a-muchos | muchos-a-muchos | uno-a-uno
```

### Formatos de Intercambio
- **JSON:** Para APIs REST
- **YAML:** Para configuración
- **CSV:** Para datos bulk

---

## 3. Lógica y Excepciones

### Flujo Principal

```
1. [Paso 1] → Descripción
2. [Paso 2] → Descripción
3. [Paso 3] → Descripción
```

### Casos de Error

| Código | Condición | Causa Raíz | Acción |
|--------|-----------|------------|--------|
| ERR_001 | [Condición] | [Causa] | [Acción] |
| ERR_002 | [Condición] | [Causa] | [Acción] |

### Manejo de Excepciones

```python
# Ejemplo de implementación correcta
try:
    operacion_critica()
except ValidationError as e:
    logging.error(f"[ERR_001] Validación fallida: {e}")
    # El cliente envió datos malformados, notificar y sugerir corrección
    raise APIError("Datos inválidos", code="ERR_001") from e
except ConnectionTimeout as e:
    logging.error(f"[ERR_002] Timeout de conexión: {e}")
    # El servicio externo no respondió, reintentar con backoff
    retry_with_backoff(max_attempts=3)
except Exception as e:
    logging.error(f"[CAUSA_RAÍZ] Error inesperado en modulo X: {e}")
    # Error no mapeado, registrar para análisis posterior
    raise InternalError("Error interno") from e
```

---

## 4. Criterios de Aceptación

### Funcionales

- [ ] Criterio 1
- [ ] Criterio 2
- [ ] Criterio 3

### No Funcionales

- **Rendimiento:** [Métrica, ej: < 200ms p95]
- **Disponibilidad:** [Métrica, ej: 99.9%]
- **Seguridad:** [Requisitos, ej: auth required]

### Casos de Prueba

| ID | Descripción | Entrada | Salida Esperada | Estado |
|----|-------------|---------|-----------------|--------|
| TC_01 | [Caso] | [Input] | [Output] | [OK/Pendiente] |
| TC_02 | [Caso] | [Input] | [Output] | [OK/Pendiente] |

---

## 5. Notas de Implementación

[Notas técnicas, decisiones de diseño, advertencias]

---

*Plantilla SDD v1.0 - Sistema SOA*