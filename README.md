# 📈 Generador de Reportes de Inteligencia de Mercado Automotor

Este proyecto demuestra la automatización de un flujo de trabajo de análisis de datos utilizando Python. A partir de una base de datos de vehículos en formato Excel, el script realiza un análisis completo del mercado, genera visualizaciones clave y consolida toda la información en un informe gerencial profesional en formato PDF.

---

## 🚀 **Resultados Obtenidos**

El script genera automáticamente un informe en PDF con los siguientes análisis visuales, permitiendo una rápida interpretación del estado del mercado.

### 1. Valor Promedio por Marca
Este gráfico compara el posicionamiento de precios entre las diferentes marcas, identificando a los líderes del mercado en términos de valor.

![Gráfico de Valor Promedio por Marca](grafico_valor_marca.png)

### 2. Distribución de Vehículos por Año
Permite entender la composición y antigüedad del parque automotor analizado, mostrando la concentración de modelos por año.

![Gráfico de Distribución por Año](grafico_distribucion_anio.png)

### 3. Top 5 Vehículos Más Valiosos
Identifica los activos de mayor valor en la base de datos, destacando los vehículos premium o de mayor demanda.

![Gráfico del Top 5 de Vehículos más Valiosos](grafico_top_5.png)

---

## 🛠️ **Tecnologías Utilizadas**

* **Python:** Lenguaje principal para toda la lógica del proyecto.
* **Pandas:** Para la manipulación y análisis eficiente de los datos desde el archivo Excel.
* **Matplotlib & Seaborn:** Para la creación de visualizaciones de datos claras y estéticas.
* **FPDF2:** Para la generación automática y maquetación del informe final en formato PDF.

---

## 📊 **Proceso de Creación del Dashboard en Excel**

Este proyecto no es solo un resultado final, sino la demostración de un flujo de trabajo completo para el tratamiento y análisis de datos enteramente dentro de Excel. El objetivo es transformar una simple lista de datos en un reporte interactivo y profesional.

El proceso se estructuró en las siguientes hojas de cálculo para mayor claridad y control:

### 1. **Hoja: `1 - Datos Crudos`**
El punto de partida. Aquí se encuentra la base de datos original sin ninguna modificación. Preservar los datos crudos es una buena práctica que garantiza la integridad de la fuente de información.

### 2. **Hoja: `2 - Limpieza y Preparación`**
En esta fase, se tomaron los datos crudos y se prepararon para el análisis:
* **Corrección de Encabezados:** Se ajustaron los nombres de las columnas para que fueran claros y profesionales (ej. `anio` -> `Año`).
* **Formato de Datos:** Se aplicó el formato de moneda a los valores para facilitar su lectura.
* **Conversión a Tabla de Excel:** El rango de datos se convirtió en una Tabla de Excel (Ctrl + T), un paso crucial que hace que los datos sean dinámicos y fáciles de manejar para las tablas dinámicas y gráficos.

### 3. **Hoja: `3 - Análisis (Tablas Dinámicas)`**
Utilizando los datos limpios, se crearon Tablas Dinámicas para resumir la información y obtener los primeros insights, como el **valor promedio de los vehículos por marca y año**.

### 4. **Hoja: `4 - Dashboard`**
Aquí es donde todos los elementos se unen para crear el reporte final:
* **Gráficos Dinámicos:** Se generaron gráficos a partir de las tablas dinámicas para visualizar las tendencias, como la evolución de los precios.
* **Segmentación de Datos (Slicers):** Se añadieron filtros interactivos para `Marca`, `Modelo` y `Año`. Esto permite al usuario explorar los datos de forma intuitiva, haciendo clic en los botones para filtrar la información que el gráfico muestra en tiempo real.

Este enfoque demuestra un proceso de análisis de datos robusto, desde la limpieza inicial hasta la creación de un dashboard interactivo y funcional.

---

## 📥 **Descargar el Archivo Final**

Para explorar el dashboard interactivo, las tablas dinámicas y todo el proceso de análisis, puedes descargar el libro de Excel completo desde el siguiente enlace:

### [➡️ **Descargar `Dashboard-de-Gestion-Automotor.xlsx`**](Dashboard-de-Gestion-Automotor.xlsx)