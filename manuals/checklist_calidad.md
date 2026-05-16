# checklist_calidad.md - Lista de Verificación de Calidad

## Verificación Pre-Entrega

### 1. Regla de Excepciones
- [ ] Ningún bloque `except:` vacío
- [ ] Ningún `except Exception: pass`
- [ ] Todo `except` tiene `logging.error()` o equivalente
- [ ] Todo `except` tiene comentario de causa raíz

### 2. Arnés de Pruebas
- [ ] Scripts de prueba ejecutados
- [ ] 100% de tests pasan
- [ ] Logs generados en `technical_core/logs/`

### 3. Documentación
- [ ] SDD actualizado con estado actual
- [ ] Comentarios inline en código complejo
- [ ] Causa raíz documentada para cada error

### 4. Nomenclatura
- [ ] Archivos en kebab-case
- [ ] Variables en snake_case
- [ ] Constantes en UPPER_SNAKE_CASE
- [ ] SDDs con formato SDD_XX_nombre.md

### 5. Trazabilidad
- [ ] Errores tienen timestamp
- [ ] Logs incluyen componente origen
- [ ] Cause raíz visible en trazas

---

## Firmar Entrega

Proyecto: _________________  
Fecha: _________________  
SDDs completados: ____/____  
Tests pass: ____%  
Excepciones vacías: 0

---

*Formato: Firmar solo cuando TODOS los checks estén marcados*