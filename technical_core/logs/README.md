# Logs de Aplicación

Este directorio contiene los logs generados por el sistema SOA y sus componentes.

## Formato de Log

```
[TIMESTAMP] [NIVEL] [COMPONENTE] [CAUSA] mensaje
```

Ejemplo:
```
[2026-05-16 10:30:00] [ERROR] [AuthModule] [TOKEN_EXPIRED] Token JWT expirado
```

## Archivos de Log

| Archivo | Descripción |
|----------|-------------|
| app.log | Log principal de la aplicación |
| test.log | Log de ejecuciones del arnés de pruebas |
| errors.log | Solo errores (para revisión rápida) |

---

*Última actualización: 2026-05-16*