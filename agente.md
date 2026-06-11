# Agente Orquestador SOA - Documentación

> Este archivo es **documentación**. El comportamiento real del agente está en `.agent/SYSTEM_PROMPT.md`.

---

## Descripción

El Agente Orquestador es el punto de entrada del sistema SOA. Gestiona dos funciones principales:

1. **Iniciar proyectos** (comando `/initsoa`)
2. **Orquestar tareas** (delegar durante el proyecto)

---

## Estructura del Agente

### Sección A: Iniciador
Inicializa proyectos nuevos desde cero con estructura completa.

**Comando:** `/initsoa`

### Sección B: Orquestador
Recibe requerimientos, carga contexto, delega al recurso apropiado.

**Flujo:** Recepción → Contexto → Planificación → Ejecución → Entrega

### Sección C: Comunes
Comandos compartidos, sistema de memoria, tipos de proyecto.

---

## Archivos de Referencia

| Archivo | Propósito |
|---------|-----------|
| `.agent/SYSTEM_PROMPT.md` | Prompt ejecutable del agente |
| `context/memory/memory.md` | Config y aprendizajes persistentes |
| `context/conversations/` | Histórico de sesiones |
| `context/knowledge/` | Datos factuales del proyecto |
| `context/metas-objetivos.md` | KPIs y hitos |
| `context/systems-architecture.md` | Reglas de oro |

---

## Tipos de Proyecto

### Técnico
- Desarrollo de software, scripts, APIs
- Estructura: `systems/`
- Validación: Arnés de pruebas
- Regla de excepciones: Obligatoria

### Genérico
- Marketing, documentación, gestión
- Estructura: `generic/`
- Validación: Checklists

---

## Nomenclatura

- Archivos/carpetas: **kebab-case**
- SDDs: `SDD_XX_nombre.md`
- Conversaciones: `YYYY-MM-DD_HHmm-resumen.md`

---

*Última actualización: 2026-06-11*