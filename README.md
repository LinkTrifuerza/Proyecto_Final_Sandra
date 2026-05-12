# Retail Data Engineering Pipeline

Este proyecto implementa un pipeline de Ingeniería de Datos (ETL) robusto diseñado para un escenario de Retail. El objetivo principal es la consolidación de fuentes de datos heterogéneas, la aplicación de técnicas de limpieza profunda y la generación de hallazgos analíticos mediante Reducción de Dimensionalidad (PCA).

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.14
- **Librerías de Datos:** Pandas, NumPy, PyArrow (formato Parquet)
- **Gestión de Bases de Datos:** SQLite3
- **Analítica Avanzada:** Scikit-Learn (StandardScaler, PCA)
- **Visualización:** Plotly (Sankey Diagram interactivo), Seaborn, Matplotlib

## Estructura del Proyecto

```text
├── fuentes/               # Datos crudos en formatos SQL, JSON, CSV, TXT, XML, XLSX
├── scripts/
│   ├── preparar_datos.py  # Inicializador del entorno y generador de datasets sintéticos
│   └── visualizaciones.py # Generador de reportes gráficos y diagramas
├── salidas/               # Artefactos procesados (Parquet), datasets finales y gráficas
├── main_pipeline.py       # Script central encargado del proceso ETL y analítica
└── README.md              # Documentación del proyecto
```

## Flujo del Pipeline

El procesamiento de la información se divide en tres capas arquitectónicas basadas en el modelo Medallion.

### Capa de Extracción (Bronze)

Ingesta de datos desde seis formatos distintos. Se destaca el uso de Expresiones Regulares (RegEx) para transformar logs de servidor no estructurados en datos tabulares de navegación.

### Capa de Procesamiento (Silver)

Ejecución de rutinas de limpieza que incluyen:

- Manejo de valores nulos.
- Eliminación de duplicados.
- Normalización de strings (limpieza de ciudades y nombres).

En esta etapa se exporta `data_master_clean.parquet` como respaldo de integridad.

### Capa Analítica (Gold)

Enriquecimiento de la información mediante:

- Segmentación avanzada (identificación del segmento **Premium Joven**).
- Aplicación de Componentes Principales (PCA) para reducir la dimensionalidad y facilitar la visualización de clusters.

El resultado optimizado se almacena en `data_master_final.parquet`.

## Entregables Visuales

El pipeline genera tres representaciones gráficas para la toma de decisiones.

### Diagrama de Sankey (HTML)

Visualización dinámica del flujo de conversión del usuario (*Customer Journey*) desde el Home hasta la Confirmación de compra.

### Boxplot de Ventas

Análisis estadístico de la distribución de montos para identificar la dispersión del ticket promedio y detectar outliers.

### Scatter Plot PCA

Representación bidimensional de los segmentos de clientes identificados tras la normalización y reducción de dimensiones.

## Instrucciones de Ejecución

Siga estos pasos para replicar el entorno y ejecutar el pipeline.

### 1. Clonar el repositorio

Clone el repositorio en su entorno local.

### 2. Instalar dependencias

```bash
pip install pandas numpy scikit-learn plotly seaborn openpyxl pyarrow
```

### 3. Ejecutar los módulos

```bash
python scripts/preparar_datos.py
python main_pipeline.py
python scripts/visualizaciones.py
```
