
# **Documentación del Código: Extracción de Información Judicial**


> .[!NOTE].
> activar el entorno virtual venv/Scripts/activate 
> instalar dependencias pip install -r requirements.txt 
> ejecutar el codigo python main.py

> .[!TIP].
>Propósito del Código

>Esta prueba practica automatiza la extracción de información judicial desde diversas páginas web. Su principal objetivo es interactuar con formularios, realizar búsquedas específicas y recolectar datos estructurados de manera eficiente y adaptable a diferentes plataformas.

>El flujo del código está diseñado para ajustarse a páginas judiciales con estructuras similares, empleando criterios definidos por el usuario y palabras clave para la búsqueda y navegación.

>---

> **Funcionalidades Principales**

>1. Selección de Formulario de Búsqueda
>- Identifica formularios específicos dentro de la página, como el tipo "por Parte".
>- Ejemplo de formularios identificables:
>  - **"histórico"**
>  - **"expediente"**
>  - **"por Parte"**
>- Detecta elementos interactivos (botones, inputs, selects) y permite establecer criterios personalizados para las búsquedas.

>2. Selección de Jurisdicción
>- Selecciona jurisdicciones específicas utilizando iniciales (ejemplo: **"com"** para Comercial).
>- Totalmente personalizable según las necesidades del usuario.

>3. Ingreso de Palabras Clave
>- Escribe automáticamente en campos de texto las palabras clave para búsquedas específicas, como por ejemplo: **"Residuos"**.
>- La palabra clave es configurable por el usuario para adaptarse a diferentes casos.

>4. Identificación y Ejecución del Botón de Envío
>- Reconoce el botón "Enviar" en el formulario y lo activa para iniciar la búsqueda.
>- **Nota:** Este proceso puede mejorarse implementando algoritmos más dinámicos que identifiquen botones similares en diferentes páginas.

>5. Navegación y Extracción de Detalles
>- Una vez cargada la nueva página:
>  - Analiza el contenido HTML para localizar eventos clave como **`mojarra.jsfcljs()`**.
>  - Este evento se utiliza para interactuar con elementos dentro de tablas.
>  - Este evento tiene una estructura que hace una extraccion diferente por cada elemento de la tabla en el codigo se logra entender perfecto

>6. Iteración y Scroll Dinámico
>- Realiza un bucle para recorrer todos los elementos de una tabla.
>- Si los elementos no son visibles, utiliza un **scroll automático** para garantizar que Selenium pueda interactuar con ellos.

>7. Navegación entre Páginas
>- Detecta y utiliza botones de "Siguiente" para pasar a nuevas tablas y continuar extrayendo datos.
>- Reinicia el índice de la tabla en cada nueva página para procesar todos los datos.

>8. Recolección Completa de Datos
>- Extrae todos los datos de las páginas y tablas disponibles.
>- **Campos adicionales que pueden incorporarse fácilmente:** 
>  - Demandante
>  - Demandado
>  - Tipo de Demanda


> **Aspectos a Mejorar**

> 1. Manejo de Captchas
>- Actualmente, el código sólo resuelve captchas tipo **click**.
>- No soporta captchas basados en imágenes o sistemas más complejos. **Esto requiere mejoras.**

>2. Optimización del Dinamismo
>- El flujo está diseñado para formularios específicos. Generalizar el manejo de diferentes formularios y estructuras puede mejorar la versatilidad del código.

> .[!IMPORTANT]. 
> 3. Pestañas Abiertas
>La pestaña del navegador debe permanecer abierta durante la ejecución del código. Cerrar la pestaña puede provocar errores intermitentes.

>4. Caida de codigo
> Si se cae el codigo se debe volver a ejecutar por culpa del captcha , algun formulario o proceso no lo pongo en bucle por miedo a baneo de ip o bloqueo
---
> .[!IMPORTANT]. 
>**Conclusión**

>Este código tiene como objetivo la extracción de datos judiciales en páginas web con estructuras similares. Con algunas mejoras adicionales, puede ampliarse para abordar casos más generales y superar limitaciones como captchas avanzados.

>Si deseas ampliar esta funcionalidad, aquí tienes algunos puntos clave para trabajar:
>1. Dinamizar el envío de formularios.
>2. Implementar un sistema para resolver captchas basados en imágenes.
>3. Integrar la extracción de datos adicionales como demandante, demandado y tipo de demanda.
>---
