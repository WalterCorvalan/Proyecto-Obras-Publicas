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

## ⚙️ **Cómo Usar este Proyecto**

Para replicar este análisis, sigue los siguientes pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [URL_DE_TU_REPOSITORIO]
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instala las dependencias necesarias:**
    ```bash
    pip install pandas matplotlib seaborn openpyxl fpdf2
    ```

4.  **Ejecuta el script principal:**
    ```bash
    python generar_reporte.py
    ```

Al finalizar, se habrán creado en la carpeta los archivos de los gráficos (`.png`) y el informe consolidado `Reporte_Mercado_Automotor.pdf`.