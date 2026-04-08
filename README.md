# Sistema SOA (Standardized Orchestration Architecture)

## ¿Qué es?

Sistema SOA es una infraestructura cognitiva diseñada para orquestar agentes de Inteligencia Artificial de manera estructurada. Elimina la fricción operativa, previene la pérdida de contexto y reduce la sobrecarga mental del usuario mediante una topología de nodos bien definida.

## Estructura del Sistema

```
sistemaSOA/
├── agente.md              # Orquestador - El cerebro operativo
├── memory/                # Memoria y cognición
│   ├── memory.md          # Registro de aprendizajes y estado
│   └── conversaciones/    # Logs de interacciones
├── contexto/              # Reglas del negocio
│   ├── systems-architecture.md  # Reglas de oro
│   ├── metas-objetivos.md      # KPIs y definición de éxito
│   └── knowledge.md            # Base de datos fáctica
├── agents/                # Agentes especializados
├── docs/                  # Salida y producción (entregables finales)
├── systems/               # Flujos de trabajo
└── manuals/               # Procedimientos operativos
```

## Principios Fundamentales

- **Fragmentación de Tareas**: Prompts monolíticos prohibidos; todo debe desglosarse en unidades lógicas ejecutables.
- **Ley de Pareto (80/20)**: Solo documentar el 20% de información que genera el 80% de decisiones correctas.
- **Fronteras Estrictas**: Lo que el agente "aprende" jamais se mezcla con lo que "produce".
- **Nomenclatura Estricta**: Uso obligatorio de kebab-case para archivos y carpetas.

## Cómo Implementar en un Nuevo Proyecto

### Opción 1: Clonar desde repositorio Git

```bash
# Crear directorio para el nuevo proyecto
mkdir mi-nuevo-proyecto
cd mi-nuevo-proyecto

# Clonar el sistema SOA
git clone https://github.com/tu-repo/sistemaSOA.git .

# O si está en tu máquina local:
git clone /ruta/a/sistemaSOA .
```

### Opción 2: Copia manual

```bash
# Copiar estructura completa
xcopy /E /I ruta\a\sistemaSOA nueva-carpeta
```

### Opción 3: Descargar ZIP

1. Ir al repositorio en GitHub
2. Hacer clic en "Code" > "Download ZIP"
3. Extraer el contenido en la carpeta del proyecto

## Primeros Pasos

1. **Editar `agente.md`**: Configurar el orquestador según el objetivo del proyecto.
2. **Actualizar `contexto/metas-objetivos.md`**: Definir KPIs y qué significa "éxito".
3. **Completar `contexto/knowledge.md`**: Añadir información relevante del negocio/producto.
4. **Revisar `contexto/systems-architecture.md`**: Ajustar reglas de oro si es necesario.

## Ciclo de Vida de una Operación

1. **Inicialización**: Definir objetivo en el orquestador (`agente.md`)
2. **Carga de Contexto**: El orquestador absorbe automáticamente los archivos de `/contexto/`
3. **Planificación**: Desglose de tareas y selección de sub-agentes
4. **Ejecución y Registro**: El trabajo se realiza; errores se guardan en `memory/memory.md`
5. **Entrega**: Output final depositado en `/docs/`, limpio y validado

## Mantenimiento

Consultar `manuals/manual-mantenimiento.md` para instrucciones sobre purga cognitiva, nomenclatura de archivos y mantenimiento general del sistema.

---

*Sistema SOA - Infraestructura cognitiva para orquestación de agentes IA*