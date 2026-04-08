# Manual de Mantenimiento - POE

## 1. Purga Cognitiva

### Cuando realizar purga
- **Frecuencia:** Mensual o cuando memory.md supere 500 lineas
- **Trigger:** Si el modelo empieza a perder contexto por tamaño

### Proceso de purga
1. Revisar memory/memory.md completo
2. Identificar:
   - Entradas redundantes -> consolidar
   - Entradas obsoletas -> eliminar
   - Entradas valiosas -> mantener
3. Crear archivo de备份 si es necesario
4. Reescribir memory.md solo con lo esencial

### Regla de oro
memory.md debe caber en una sola lectura de 5 minutos maximo.

---

## 2. Nomenclatura

### Regla general
Todo archivo y carpeta debe usar **kebab-case**:
- Minusculas
- Guiones como separadores
- Sin acentos
- Sin espacios

### Ejemplos
- Correcto: `agente-analisis-gastos.md`
- Incorrecto: `agente Analisis Gastos.md`

### Por qué
- Garantiza automatización futura
- Evita problemas de compatibilidad
- Consistencia en todo el sistema

---

## 3. Control de Archivos

### Maximo recomendado por carpeta
- `/agents/`: 50 archivos
- `/skills/`: 30 archivos
- `/docs/`: Sin limite (son outputs)

### Senales de alarma
- Mas de 100 archivos en cualquier carpeta
- Archivos sin usar en 30+ dias
- Duplicacion de funcionalidad

### Accion
Revisar y reorganizar o eliminar archivos no usados.

---

## 4. Mantenimiento del Orquestador

### Revision obligatoria
- **Frecuencia:** Trimestral
- **Que revisar:**
  - Reglas de delegacion siguen siendo validas
  - Flujo de contexto no tiene cuellos de botella
  - memory.md refleja aprendizajes reales

### Actualizacion
Si el orquestador falla repetidamente:
1. Auditar systems-architecture.md
2. Revisar si hay ambiguedades en metas-objetivos.md
3. Corregir estructura, no culpar a la IA

---

## 5. Checklist de Mantenimiento

- [ ] Revisar memory/memory.md
- [ ] Verificar nomenclatura (kebab-case)
- [ ] Eliminar archivos no usados
- [ ] Actualizar knowledge.md si hay nuevos datos
- [ ] Verificar que /docs/ solo tenga outputs validados
- [ ] Respaldar antes de purgar

---

## 6. Contacto y Escalamiento

Si el sistema tiene problemas estructurales:
1. Revisar este manual
2. Verificar systems-architecture.md
3. Si persiste, revisar principios rectores

El error esta en la estructura, no en la IA.
