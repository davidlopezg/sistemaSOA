# Changelog - Sistema SOA

Todos los cambios notables de este proyecto se documentarán en este archivo.

## [3.0.0] - 2026-06-11

### Added
- Sistema de contexto completo (memory, knowledge, metas-objetivos)
- Soporte para proyectos técnicos y genéricos
- Arnés de pruebas automatizadas (test_estructura, test_nomenclatura, test_exceptions)
- Scripts de logging para memoria y progreso
- Documentación completa con SDD templates
- CI/CD con GitHub Actions

### Fixed
- Rutas relativas corregidas en todos los scripts (ahora funcionan desde cualquier directorio)
- Nomenclatura actualizada a kebab-case
- Referencias a directorios `memory/` → `context/`

### Changed
- Estructura reorganizada con directorio `context/` central
- README mejorado con ejemplos funcionales

## [2.0.0] - 2026-05-16

### Added
- Sistema de SDDs modulares
- Comandos slash (/initsoa, /status, /save, /learn)
- Regla de excepciones obligatoria para proyectos técnicos

## [1.0.0] - 2026-05-01

### Added
- Versión inicial del sistema SOA
