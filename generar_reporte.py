import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import time

# --- FASE 1: Análisis y Generación de Gráficos ---

def analizar_y_crear_graficos(archivo_excel):
    """
    Lee el archivo Excel, realiza varios análisis y guarda los gráficos como imágenes.
    Retorna una lista con los nombres de los archivos de los gráficos generados.
    """
    try:
        df = pd.read_excel(archivo_excel)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{archivo_excel}'.")
        return None, None

    # --- Análisis 1: Valor Promedio por Marca ---
    plt.figure(figsize=(10, 6))
    valor_promedio_marca = df.groupby('marca')['valor'].mean().sort_values(ascending=False)
    sns.barplot(x=valor_promedio_marca.index, y=valor_promedio_marca.values, palette='viridis')
    plt.title('Valor Promedio de Vehículo por Marca', fontsize=16)
    plt.ylabel('Valor Promedio (AR$)')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    grafico1_path = 'grafico_valor_marca.png'
    plt.savefig(grafico1_path)
    plt.close()
    print(f"-> Gráfico 1 guardado: {grafico1_path}")

    # --- Análisis 2: Distribución de Vehículos por Año ---
    plt.figure(figsize=(10, 6))
    sns.histplot(df['anio'], bins=len(df['anio'].unique()), kde=False, color='skyblue')
    plt.title('Distribución de Vehículos por Año de Modelo', fontsize=16)
    plt.xlabel('Año')
    plt.ylabel('Cantidad de Modelos')
    plt.tight_layout()
    grafico2_path = 'grafico_distribucion_anio.png'
    plt.savefig(grafico2_path)
    plt.close()
    print(f"-> Gráfico 2 guardado: {grafico2_path}")

    # --- Análisis 3: Top 5 Vehículos más Valiosos ---
    df['vehiculo'] = df['marca'] + ' ' + df['modelo'] + ' (' + df['anio'].astype(str) + ')'
    top_5 = df.sort_values('valor', ascending=False).head(5)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_5['valor'], y=top_5['vehiculo'], palette='rocket')
    plt.title('Top 5 Vehículos Más Valiosos', fontsize=16)
    plt.xlabel('Valor (AR$)')
    plt.ylabel('')
    plt.tight_layout()
    grafico3_path = 'grafico_top_5.png'
    plt.savefig(grafico3_path)
    plt.close()
    print(f"-> Gráfico 3 guardado: {grafico3_path}")

    # Recopilar estadísticas para el texto del informe
    estadisticas = {
        "total_vehiculos": len(df),
        "valor_promedio_total": df['valor'].mean(),
        "marca_mas_valiosa": valor_promedio_marca.index[0],
        "valor_marca_mas_valiosa": valor_promedio_marca.iloc[0]
    }
    
    return [grafico1_path, grafico2_path, grafico3_path], estadisticas

# --- FASE 2: Creación del Informe PDF ---

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Informe Gerencial - Mercado Automotor', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        fecha = time.strftime("%d/%m/%Y")
        self.cell(0, 10, f'Página {self.page_no()} | Generado el {fecha}', 0, 0, 'C')

def crear_informe_pdf(lista_graficos, estadisticas):
    """
    Crea un archivo PDF que incluye el texto del análisis y los gráficos.
    """
    pdf = PDF()
    pdf.add_page()
    
    # --- Texto del Informe ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '1. Resumen Ejecutivo del Análisis', 0, 1, 'L')
    
    pdf.set_font('Arial', '', 11)
    texto_resumen = (
        f"El presente informe analiza la base de datos de valuación de vehículos, que contiene un total de "
        f"{estadisticas['total_vehiculos']} registros. El valor promedio de un vehículo en el mercado analizado "
        f"es de AR$ {estadisticas['valor_promedio_total']:,.2f}.\n\n"
        f"La marca con el mayor valor promedio de sus vehículos es **{estadisticas['marca_mas_valiosa']}**, "
        f"alcanzando una media de AR$ {estadisticas['valor_marca_mas_valiosa']:,.2f}."
    )
    pdf.multi_cell(0, 6, texto_resumen)
    pdf.ln(10)

    # --- Inserción de Gráficos ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '2. Análisis Visual del Mercado', 0, 1, 'L')
    
    for i, grafico in enumerate(lista_graficos):
        pdf.image(grafico, x=None, y=None, w=180) # w=180 para ajustar al ancho de la página
        pdf.ln(5)

    nombre_pdf = 'Reporte_Mercado_Automotor.pdf'
    pdf.output(nombre_pdf)
    print(f"\n✅ ¡Éxito! Informe PDF generado: {nombre_pdf}")

# --- FASE 3: Ejecución Principal ---

if __name__ == "__main__":
    archivo_excel_datos = 'tabla_valuacion.xlsx'
    
    print("Iniciando generación de reporte...")
    graficos, estadisticas = analizar_y_crear_graficos(archivo_excel_datos)
    
    if graficos and estadisticas:
        crear_informe_pdf(graficos, estadisticas)