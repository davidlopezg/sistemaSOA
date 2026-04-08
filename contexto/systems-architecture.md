# Systems Architecture - Reglas de Oro del Sistema SOA

## Principios Rectores

### 1. Fragmentacion de Tareas (Micro-estructuracion)
Ningun agente debe recibir un prompt monolitico. Toda instruccion compleja debe desglosarse en su minima unidad logica ejecutable.

**Aplicacion:**
- Cada tarea debe poder completarse en maximo 3 iteraciones
- Si una tarea requiere mas, fragmentar en sub-tareas
- Ningun prompt mayor a 500 palabras

### 2. Ley de Pareto (80/20) en el Contexto
Solo se documenta en `knowledge.md` y este archivo el 20% de la informacion que genera el 80% de las decisiones correctas del agente.

**Aplicacion:**
- Evitar sobrecarga de datos
- Documentar solo lo esencial
- La sobrecarga de datos colapsa la memoria

### 3. Ley de Parkinson en la Ejecucion
Los agentes y sistemas deben tener limites claros de output y alcance. No se permite la iteracion infinita sin revision.

**Aplicacion:**
- Maximo 3 intentos por tarea antes de escalamiento
- Fechas limite para cada fase
- Revision obligatoria antes de pasar a produccion

### 4. Fronteras Estrictas (Aislamiento de Dominio)
Lo que el agente "aprende" o "procesa" jams se mezcla con lo que el agente "produce".

**Aplicacion:**
- Memoria y documentacion final viven en ecosistemas separados
- `/memory/` = input y proceso
- `/docs/` = output validado
- Separacion estricta: nunca cruzar flujos

---

## Restricciones Eticas y de Formato

1. Sin datos crudos en el orquestador
2. Sin output directo desde el orquestador
3. Todo pasa por delegacion
4. Validacion obligatoria antes de /docs/

---

## Principios Operativos

- Nomenclatura: siempre kebab-case
- Extension maxima de archivos: revisar regularmente
- Purga cognitiva: segun manual-mantenimiento.md
- Tolerancia cero a laambigüedad: el error esta en la estructura, no en la IA
