# Contribuir a Sistema SOA

¡Gracias por tu interés en contribuir!

## Cómo contribuir

### 1. Reportar bugs
Crea un issue con:
- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Versión del sistema

### 2. Sugerir features
Abre un issue con:
- Descripción de la feature
- Caso de uso
- Alternativas consideradas

### 3. Pull Requests
1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/mi-feature`)
3. Haz tus cambios
4. Ejecuta los tests: `python technical_core/arnes_tests/test_*.py`
5. Commit con mensajes claros
6. Push y abre PR

## Reglas

### Nomenclatura
- Archivos/carpetas: `kebab-case`
- SDDs: `SDD_XX_nombre.md`
- Variables: `snake_case`
- Clases: `PascalCase`

### Excepciones (proyectos técnicos)
```python
# ❌ PROHIBIDO
try:
    operacion()
except:
    pass

# ✅ CORRECTO
try:
    operacion()
except SpecificError as e:
    logging.error(f"[CAUSA] {e}")
    raise
```

### Tests
Todos los PR deben pasar:
```bash
python technical_core/arnes_tests/test_estructura.py
python technical_core/arnes_tests/test_nomenclatura.py
python technical_core/arnes_tests/test_exceptions.py
```

## Estructura de commits

```
feat: nueva feature
fix: bug fix
docs: cambios en documentación
refactor: refactorización
test: agregar tests
chore: mantenimiento
```

---

*¡Tu contribución hace Sistema SOA mejor para todos!*
