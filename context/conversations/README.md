# memory/conversaciones/ - Log Completo de Sesiones

## Propósito

Guardar el transcript completo de cada conversación usuario-agente.
Este directorio es un log histórico - no se lee durante el trabajo normal.

## Formato de Archivo

```
YYYY-MM-DD_HHmm-[resumen-corto].md
```

Ejemplos:
- `2026-05-16_1030-inicializacion-soa.md`
- `2026-05-17_1430-servicio-auth.md`
- `2026-05-18_0915-revision-codigo.md`

## Cuándo Guardar

- Al final de cada sesión significativa
- Antes de cerrar sesión larga
- Cuando el usuario lo solicite

## Formato del Log

```markdown
# Conversación: YYYY-MM-DD HH:MM - Resumen

## Usuario
[Nombre/Alias del usuario]

## Inicio
[Fecha y hora de inicio]

## Tema
[Qué se estaba trabajando]

## Resumen
[Qué se hizo, qué se decidió, qué quedó pendiente]

## Archivos Modificados
- [archivo.md]
- [script.py]

## Pendientes
- [Tarea 1]
- [Tarea 2]

## Fin
[Fecha y hora de cierre]

---
*Sesión guardada automáticamente por agente*
```

## Ejemplo de Nombre

```
2026-05-16_1030-inicializacion-soa.md
 └────── ───── ─────────────────
   │       │          │
   │       │          └─ Resumen corto (kebab-case)
   │       │
   │       └─ Hora (HHMM)
   │
   └─ Fecha
```

---

## Gestión de Espacio

Si el directorio crece mucho (> 50 archivos):
1. El agente puede archivar los más antiguos en subcarpetas `YYYY/`
2. O preguntar al usuario si quiere un resumen consolidado

---

*Esta carpeta es solo para logs - leer no es necesario durante trabajo normal*