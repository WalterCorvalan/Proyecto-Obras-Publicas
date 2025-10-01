import pandas as pd

# --- FASE 1: Datos de Referencia ---
# Ya no tenemos la tabla aquí. En su lugar, definimos el nombre del archivo.
ARCHIVO_VALUACION = 'tabla_valuacion.xlsx'

# La tabla de costos sigue aquí porque es una configuración del programa.
COSTOS_TRANSFERENCIA = {
    'arancel_nacional': 0.015,
    'arancel_provincial': 0.02,
    'tasa_administrativa_fija': 45000.00,
    'impuesto_sellos': 0.01,
}

# --- FASE 2: Lógica de la Calculadora (Actualizada) ---

def buscar_valor_vehiculo(marca, modelo, anio):
    """
    Busca el valor de un vehículo leyendo los datos desde el archivo Excel.
    """
    try:
        df = pd.read_excel(ARCHIVO_VALUACION)
    except FileNotFoundError:
        # Si el archivo no existe, damos un mensaje de error claro.
        print(f"ERROR: No se encontró el archivo '{ARCHIVO_VALUACION}'.")
        print("Por favor, ejecuta primero el script 'crear_excel.py' para generarlo.")
        return None

    # Usamos filtros de pandas para buscar el vehículo (más eficiente)
    vehiculo = df[
        (df['marca'].str.lower() == marca.lower()) &
        (df['modelo'].str.lower() == modelo.lower()) &
        (df['anio'] == anio)
    ]
    
    if not vehiculo.empty:
        # Si se encontró, devolvemos el valor de la primera fila coincidente
        return vehiculo.iloc[0]['valor']
    
    return None # Si no se encuentra, devolvemos None

# El resto de las funciones no necesitan cambios
def calcular_costos_transferencia(valor_vehiculo):
    """Calcula el desglose de costos de transferencia basado en el valor del vehículo."""
    if valor_vehiculo is None or valor_vehiculo <= 0:
        return {}
    costos_desglosados = {
        'Arancel Nacional (1.5%)': valor_vehiculo * COSTOS_TRANSFERENCIA['arancel_nacional'],
        'Arancel Provincial (2.0%)': valor_vehiculo * COSTOS_TRANSFERENCIA['arancel_provincial'],
        'Impuesto de Sellos (1.0%)': valor_vehiculo * COSTOS_TRANSFERENCIA['impuesto_sellos'],
        'Tasas Administrativas (Fijo)': COSTOS_TRANSFERENCIA['tasa_administrativa_fija']
    }
    costos_desglosados['Costo Total de Transferencia'] = sum(costos_desglosados.values())
    return costos_desglosados

def generar_informe_de_gestion(marca, modelo, anio):
    """Crea un informe completo y profesional de valuación y costos."""
    print(f"--- INFORME DE GESTIÓN: TRANSFERENCIA DE VEHÍCULO ---")
    print(f"Vehículo Consultado: {marca.title()} {modelo.title()} ({anio})")
    print("---------------------------------------------------------")
    
    valor_fiscal = buscar_valor_vehiculo(marca, modelo, anio)
    
    if valor_fiscal is None:
        print("\nERROR: Vehículo no encontrado en la tabla de valuaciones.")
        return
        
    print(f"1. VALUACIÓN FISCAL DEL ACTIVO")
    print(f"   - Valor según tabla de referencia: AR$ {valor_fiscal:,.2f}\n")
    
    costos = calcular_costos_transferencia(valor_fiscal)
    
    print(f"2. DESGLOSE DE COSTOS DE TRANSFERENCIA")
    for concepto, monto in costos.items():
        print(f"   - {concepto:<30} AR$ {monto:>15,.2f}")
        
    print("---------------------------------------------------------")
    print("Este reporte automatiza la consulta y cálculo de costos,")
    print("demostrando la capacidad de transformar normativas en herramientas de gestión.")

# --- FASE 3: Simulación de un Caso de Uso ---
if __name__ == "__main__":
    # Ahora puedes probar con cualquier vehículo de tu nuevo Excel
    generar_informe_de_gestion('Volkswagen', 'Amarok', 2022)
    print("\n" + "="*50 + "\n")
    generar_informe_de_gestion('Peugeot', '208', 2021)