# MANUAL_MANTENIMIENTO.md - Guía de Mantenimiento del Sistema

## Resumen

Este documento describe cómo mantener y evolucionar el sistema SOA a lo largo del tiempo.

---

## 1. Actualizar el Sistema

### Nueva versión del sistema

Cuando se actualice el sistema SOA:

1. Documentar cambios en `CHANGELOG.md` (crear si no existe)
2. Actualizar versión en:
   - `.agent/SYSTEM_PROMPT.md`
   - `agente.md`
   - `memory/memory.md`
   - `contexto/systems-architecture.md`

### Agregar nuevos comandos

1. Definir comando en `.agent/SYSTEM_PROMPT.md`
2. Documentar en `agente.md` (tabla de comandos)
3. Actualizar `README.md` (tabla de comandos)
4. Actualizar `docs/GUIA_RAPIDA.md`

---

## 2. Gestión de Memoria

### Limpiar conversaciones antiguas

Cuando `memory/conversaciones/` tenga > 50 archivos:

1. Crear subcarpeta `YYYY/` (año actual)
2. Mover archivos antiguos
3. O preguntar al usuario si quiere un resumen consolidado

### Consolidar aprendizajes

Periódicamente:
1. Revisar `memory/memory.md`
2. Eliminar entradas obsoletas
3. Mantener solo aprendizajes relevantes

---

## 3. Gestionar SDDs

### Archivar SDDs completados

Cuando un SDD está en estado "Completado" o "Producción":

1. Mover a subcarpeta `completed/` dentro de `systems/` o `generic/sdds/`
2. Actualizar referencia en `MASTER_PLAN.md`

### Eliminar SDDs obsoletos

1. Documentar por qué se elimina en `memory/memory.md`
2. Eliminar archivo
3. Actualizar `MASTER_PLAN.md`

---

## 4. Nomenclatura

### Archivos
- Usar **kebab-case**: `mi-archivo.md`
- NO usar espacios ni caracteres especiales

### SDDs
- Formato: `SDD_XX_nombre.md` donde XX es número secuencial
- Ejemplo: `SDD_01_autenticacion.md`, `SDD_02_api_rest.md`

### Conversaciones
- Formato: `YYYY-MM-DD_HHmm-resumen.md`
- Ejemplo: `2026-05-16_1030-inicializacion-soa.md`

---

## 5. Scripts

### Actualizar scripts existentes

Si se modifica un script:
1. Verificar que sigue la regla de excepciones
2. Probar que funciona correctamente
3. Actualizar README en la carpeta correspondiente

### Crear nuevos scripts

1. Seguir formato de scripts existentes
2. Incluir docstring con uso
3. Incluir manejo de excepciones con logging
4. Documentar en `technical_core/scripts/README.md` o `generic/scripts/README.md`

---

## 6. Templates

### Actualizar plantillas SDD

Si se modifica una plantilla SDD:
1. Documentar cambio en el header de la plantilla
2. NO afectar SDDs ya creados (son inmutables una vez creados)
3. Los SDDs existentes mantienen su versión de plantilla original

---

## 7. Backup y Sincronización

### Antes de cambios mayores

1. Hacer commit de cambios
2. Verificar que todo está en git
3. Si es posible, hacer backup

### Sincronización entre máquinas

1. Clonar repositorio
2. Ejecutar `/initsoa` si es proyecto nuevo
3. O simplemente continuar (el sistema es idempotente)

---

## 8. Troubleshooting

### El agente no reconoce comandos

1. Verificar que `.agent/SYSTEM_PROMPT.md` existe
2. Verificar que `agente.md` está actualizado
3. Revisar que el agente haya leído el archivo

### Scripts no funcionan

1. Verificar Python instalado: `python3 --version`
2. Verificar permisos de ejecución
3. Revisar logs en `/technical_core/logs/`

### Arnés de pruebas falla

1. Leer mensaje de error completo
2. Corregir problema reportado
3. Volver a ejecutar hasta que pase

---

*Última actualización: 2026-05-16*