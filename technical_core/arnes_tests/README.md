# ARNÉS DE PRUEBAS - Sistema SOA

## Propósito

Contiene scripts de validación para verificar que el código generado cumple los estándares de calidad antes de ser entregado.

## Estructura

```
arnes_tests/
├── data/           # Datos de prueba
│   ├── sample_input.json
│   └── test_cases.yaml
├── logs/           # Logs de ejecución
│   └── app.log
├── test_exceptions.py    # Valida regla de excepciones
├── test_nomenclatura.py  # Valida naming conventions
└── test_estructura.py    # Valida estructura de archivos
```

## Uso

```bash
# Ejecutar todos los tests
python -m pytest arnes_tests/ -v

# Ejecutar test específico
python -m pytest arnes_tests/test_exceptions.py -v

# Ver logs
cat arnes_tests/logs/app.log
```

## Scripts Disponibles

### test_exceptions.py
Verifica que NO existan excepciones vacías en el código.

### test_nomenclatura.py
Verifica naming conventions (kebab-case, snake_case, etc.).

### test_estructura.py
Verifica que la estructura de carpetas sea correcta.

---

*Última actualización: 2026-05-16*