import pandas as pd
import sqlite3
import json
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def ejecutar_etl_completo():
    print("Iniciando procesamiento ETL...")

    # 1. EXTRACCIÓN
    conn = sqlite3.connect('fuentes/ventas_retail.db')
    df_ventas = pd.read_sql('SELECT * FROM ventas_historicas', conn)
    conn.close()

    with open('fuentes/perfiles_usuarios.json', 'r') as f:
        df_perfiles = pd.DataFrame(json.load(f))

    # 2. ENRIQUECIMIENTO (Join)
    df_master = pd.merge(df_ventas, df_perfiles, left_on='id_cliente', right_on='Customer_ID', how='inner')

    # 3. REGLAS DE NEGOCIO (Aquí es donde se crea la columna que faltaba)
    # Si el gasto es > 400 y la edad < 30, es Premium Joven, si no, Estándar
    df_master['segmento_cliente'] = np.where(
        (df_master['monto'] > 400) & (df_master['edad'] < 30), 
        'Premium Joven', 
        'Estándar'
    )

    # 4. PCA (Reducción de dimensiones)
    # Escalamos para que el PCA no se sesgue
    features = ['monto', 'edad', 'ingresos']
    x = StandardScaler().fit_transform(df_master[features])
    
    pca = PCA(n_components=2)
    componentes = pca.fit_transform(x)
    
    # Agregamos los resultados al dataframe
    df_master['pca_1'] = componentes[:, 0]
    df_master['pca_2'] = componentes[:, 1]

    # 5. EXPORTACIÓN FINAL
    df_master.to_parquet('salidas/data_master_final.parquet', index=False)
    print("¡Archivo maestro generado con éxito en 'salidas/data_master_final.parquet'!")

if __name__ == "__main__":
    ejecutar_etl_completo()