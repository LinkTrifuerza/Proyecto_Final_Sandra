import pandas as pd
import re
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generar_reporte_visual():
    print("Generando entregables visuales...")
    os.makedirs('salidas', exist_ok=True)

    # --- 1. GRÁFICO DE SANKEY (Basado en Logs) ---
    logs_rutas = []
    patron = r"Access to (?P<ruta>.*?) -"
    
    if os.path.exists('fuentes/logs_servidor.txt'):
        with open('fuentes/logs_servidor.txt', 'r') as f:
            for linea in f:
                match = re.search(patron, linea)
                if match: logs_rutas.append(match.group('ruta'))
        
        df_logs = pd.Series(logs_rutas).value_counts()
        etiquetas = ["Home", "Catalogo", "Carrito", "Checkout", "Confirmacion"]
        
        fig_sankey = go.Figure(data=[go.Sankey(
            node = dict(pad=15, thickness=20, label=etiquetas, color="royalblue"),
            link = dict(
                source=[0, 1, 2, 3], 
                target=[1, 2, 3, 4],
                value=[df_logs.get('Home', 0), df_logs.get('Catalogo', 0), 
                       df_logs.get('Carrito', 0), df_logs.get('Checkout', 0)]
            ))])
        fig_sankey.update_layout(title_text="Flujo de Navegación del Usuario", font_size=12)
        fig_sankey.write_html("salidas/sankey_flujo.html")
        print("- Sankey Diagram generado en 'salidas/sankey_flujo.html'")

    # --- 2. BOXPLOT Y PCA (Basados en el archivo maestro) ---
    if os.path.exists('salidas/data_master_final.parquet'):
        df = pd.read_parquet('salidas/data_master_final.parquet')

        # Boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df['monto'], color='skyblue')
        plt.title('Distribución de Montos y Outliers')
        plt.savefig('salidas/boxplot_ventas.png')
        print("- Boxplot generado en 'salidas/boxplot_ventas.png'")

        # Scatter PCA
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='pca_1', y='pca_2', hue='segmento_cliente')
        plt.title('Clusters de Comportamiento (PCA)')
        plt.savefig('salidas/scatter_pca.png')
        print("- Scatter Plot PCA generado en 'salidas/scatter_pca.png'")

if __name__ == "__main__":
    generar_reporte_visual()