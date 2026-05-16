# SDD_01_ejemplo.md - Módulo de Ejemplo

> ⚠️ Este es un SDD de ejemplo. Eliminar después de crear SDDs reales.

---

## 1. Alcance

**ID:** SDD_01  
**Nombre:** Módulo de Ejemplo  
**Versión:** 1.0  
**Estado:** Borrador  
**Fecha:** YYYY-MM-DD

### Descripción
Este SDD demuestra la estructura para documentar módulos del proyecto.
Reemplazar con información real del proyecto.

### Tipo de Proyecto
- [ ] Técnico
- [ ] Genérico

### Stakeholders
- [Nombre]: [Rol]

---

## 2. Recursos (Genérico) / Estructura de Datos (Técnico)

### Genérico:
| Recurso | Detalle |
|---------|---------|
| Persona | [Responsable] |
| Herramienta | [Tool] |
| Presupuesto | [€] |

### Técnico:
```yaml
entidad:
  campos:
    - nombre: string
    - tipo: string
```

---

## 3. Plan de Trabajo / Flujo Principal

### Fases

| Fase | Descripción | Fecha | Estado |
|------|-------------|-------|--------|
| 1 | [Nombre] | YYYY-MM-DD | [ ] |
| 2 | [Nombre] | YYYY-MM-DD | [ ] |

---

## 4. Problemas y Soluciones / Excepciones

### Genérico:
| Problema | Probabilidad | Impacto | Solución |
|----------|--------------|---------|----------|
| [Problema] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Solución] |

### Técnico:
```python
try:
    operacion()
except Error as e:
    logging.error(f"[CAUSA] {e}")
    # Hacer algo
```

---

## 5. Criterios de Éxito

### Checklist de Entrega
- [ ] Criterio 1
- [ ] Criterio 2

### Métricas
| Métrica | Objetivo | Actual | Estado |
|---------|----------|--------|--------|
| [Métrica] | [Valor] | [Valor] | [OK/En riesgo] |

---

## 6. Notas

[Notas importantes del módulo]

---

## 7. Historial

| Fecha | Cambio | Responsable |
|-------|--------|-------------|
| YYYY-MM-DD | Creación | [Nombre] |

---

*SDD de ejemplo - Eliminar después de crear SDDs reales*