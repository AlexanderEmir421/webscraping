# Documentación del Código: Extracción de Información Judicial

> **Nota:**
> - Crear un entorno virtual: `python -m venv venv` 
> - Activar el entorno virtual: `venv/Scripts/activate`
> - Instalar dependencias: `pip install -r requirements.txt`
> - Ejecutar el código: `python main.py`

---

## Propósito del Código

Esta prueba práctica automatiza la extracción de información judicial desde diversas páginas web. Su principal objetivo es interactuar con formularios, realizar búsquedas específicas y recolectar datos estructurados de manera eficiente y adaptable a diferentes plataformas.

El flujo del código está diseñado para ajustarse a páginas judiciales con estructuras similares, empleando criterios definidos por el usuario y palabras clave para la búsqueda y navegación.

---

## Funcionalidades Principales

### 1. Selección de Formulario de Búsqueda
- Identifica formularios específicos dentro de la página, como el tipo "por Parte".  
  Ejemplo de formularios identificables:
  - "histórico"
  - "expediente"
  - "por Parte"
- Detecta elementos interactivos (botones, inputs, selects) y permite establecer criterios personalizados para las búsquedas.

### 2. Selección de Jurisdicción
- Selecciona jurisdicciones específicas utilizando iniciales (ejemplo: "com" para Comercial).  
- Totalmente personalizable según las necesidades del usuario.

### 3. Ingreso de Palabras Clave
- Escribe automáticamente en campos de texto las palabras clave para búsquedas específicas, como por ejemplo: `Residuos`.
- La palabra clave es configurable por el usuario para adaptarse a diferentes casos.

### 4. Identificación y Ejecución del Botón de Envío
- Reconoce el botón "Enviar" en el formulario y lo activa para iniciar la búsqueda.  
  > **Nota:** Este proceso puede mejorarse implementando algoritmos más dinámicos que identifiquen botones similares en diferentes páginas.

---

## Aspectos a Mejorar

### Manejo de Captchas
- Actualmente, el código sólo resuelve captchas tipo click.
- No soporta captchas basados en imágenes o sistemas más complejos. Esto requiere mejoras.

### Optimización del Dinamismo
- El flujo está diseñado para formularios específicos. Generalizar el manejo de diferentes formularios y estructuras puede mejorar la versatilidad del código.

---

## Conclusión

Este código tiene como objetivo la extracción de datos judiciales en páginas web con estructuras similares. Con algunas mejoras adicionales, puede ampliarse para abordar casos más generales y superar limitaciones como captchas avanzados.

> **Importante:**  
> - La pestaña del navegador debe permanecer abierta durante la ejecución del código. Cerrar la pestaña puede provocar errores.  
> - Si el código se cae debido a captchas o errores en formularios, es necesario volver a ejecutarlo. Evité implementar bucles automáticos para evitar bloqueos o baneos de IP.
