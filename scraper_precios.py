import os
from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup


def obtener_datos_catalogo():
    """Simula la extracción de productos desde un e-commerce o API.

    Reemplazar la URL objetivo según el caso de uso real.
    """
    # Usamos datos de muestra estructurados para garantizar ejecución inmediata
    productos_demo = [
        {"id": "PROD-01", "producto": "Teclado Mecánico RGB", "categoria": "Periféricos", "precio_competencia": 45000, "stock": True},
        {"id": "PROD-02", "producto": "Mouse Inalámbrico Pro", "categoria": "Periféricos", "precio_competencia": 28000, "stock": True},
        {"id": "PROD-03", "producto": "Monitor 24 FHD 165Hz", "categoria": "Monitores", "precio_competencia": 185000, "stock": False},
        {"id": "PROD-04", "producto": "Auriculares Gamer 7.1", "categoria": "Audio", "precio_competencia": 62000, "stock": True},
        {"id": "PROD-05", "producto": "Pad Mouse XL Control", "categoria": "Periféricos", "precio_competencia": 12000, "stock": True},
    ]
    return productos_demo


def procesar_y_analizar(datos):
    """Convierte la lista en DataFrame, aplica transformaciones y genera alertas."""
    df = pd.DataFrame(datos)

    # Agregar fecha de captura
    df["fecha_recoleccion"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Definir lógica de negocio: alerta de stock
    df["estado_alerta"] = df["stock"].apply(
        lambda x: "Disponible" if x else "Sin Stock en Competencia"
    )

    return df


def exportar_reporte(df, formato="csv"):
    """Exporta los datos procesados a la carpeta de salida."""
    os.makedirs("output", exist_ok=True)
    fecha_str = datetime.now().strftime("%Y%m%d_%H%M")

    if formato == "excel":
        ruta_archivo = f"output/reporte_precios_{fecha_str}.xlsx"
        df.to_excel(ruta_archivo, index=False)
    else:
        ruta_archivo = f"output/reporte_precios_{fecha_str}.csv"
        df.to_csv(ruta_archivo, index=False, encoding="utf-8-sig")

    print(f"✅ Reporte generado con éxito en: {ruta_archivo}")


if __name__ == "__main__":
    print("🚀 Iniciando extracción automatizada de precios...")
    raw_data = obtener_datos_catalogo()
    df_procesado = procesar_y_analizar(raw_data)

    print("\n--- Vista Previa de los Datos Procesados ---")
    print(df_procesado[["id", "producto", "precio_competencia", "estado_alerta"]])

    exportar_reporte(df_procesado, formato="csv")
