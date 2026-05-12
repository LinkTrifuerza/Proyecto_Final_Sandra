import pandas as pd
import numpy as np
import sqlite3
import json
import os
import xml.etree.ElementTree as ET

# Definir carpetas de trabajo
os.makedirs('fuentes', exist_ok=True)
os.makedirs('salidas', exist_ok=True)

print("Iniciando creación de entorno de datos desde cero...")

# 1. SQL: Ventas Históricas (8,000 registros)
conn = sqlite3.connect('fuentes/ventas_retail.db')
df_ventas = pd.DataFrame({
    'id_transaccion': range(1, 8001),
    'id_cliente': [f"CUST-{np.random.randint(1000, 2000)}" for _ in range(8000)],
    'monto': np.random.uniform(10, 500, 8000).round(2),
    'fecha': ['2026-05-10'] * 8000,
    'id_tienda': [f"Tienda_{np.random.randint(1,10)}" for _ in range(8000)]
})
df_ventas.to_sql('ventas_historicas', conn, if_exists='replace', index=False)
conn.close()

# 2. JSON: Perfiles (Simulación NoSQL)
perfiles = [{"Customer_ID": f"CUST-{i}", "edad": int(np.random.randint(18, 70)), 
             "ingresos": float(np.random.uniform(10000, 80000)), 
             "ciudad": np.random.choice(['CDMX', 'mx', 'mex', 'Monterrey'])} for i in range(1000, 2001)]
with open('fuentes/perfiles_usuarios.json', 'w') as f:
    json.dump(perfiles, f)

# 3. CSV: Inventario (Con nulos y duplicados para limpieza)
n_inv = 600
df_inv = pd.DataFrame({'id': range(1, n_inv + 1), 'stock': np.random.randint(0, 100, n_inv)})
df_inv.loc[0:50, 'stock'] = np.nan # Insertar nulos
df_inv = pd.concat([df_inv, df_inv.iloc[:30]], ignore_index=True) # Insertar duplicados
df_inv.to_csv('fuentes/inventario.csv', index=False)

# 4. TXT: Logs del Servidor (Para RegEx y Sankey)
rutas = ['Home', 'Catalogo', 'Carrito', 'Checkout', 'Confirmacion']
with open('fuentes/logs_servidor.txt', 'w') as f:
    for _ in range(3000):
        ruta = np.random.choice(rutas)
        nivel = "INFO" if np.random.random() > 0.1 else "ERROR"
        f.write(f"[2026-05-12 08:00:00] {nivel} - Access to {ruta} - Latency: {np.random.randint(50, 500)}ms\n")

# 5. XML: Catálogos de Productos (NUEVO)
root = ET.Element("catalogos")
for i, cat in enumerate(["Electrónica", "Ropa", "Hogar", "Deportes"]):
    item = ET.SubElement(root, "categoria", id=str(i+1))
    item.text = cat
tree = ET.ElementTree(root)
tree.write("fuentes/catalogos.xml", encoding='utf-8', xml_declaration=True)

# 6. XLSX: Metas Anuales (NUEVO - Requiere openpyxl)
df_metas = pd.DataFrame({
    'Region': ['Norte', 'Sur', 'Centro', 'Occidente'],
    'Meta_Ventas': [1000000, 800000, 1500000, 950000]
})
df_metas.to_excel('fuentes/metas_anuales.xlsx', index=False)

print("¡Éxito! Todos los archivos fuente han sido generados desde cero en la carpeta /fuentes.")