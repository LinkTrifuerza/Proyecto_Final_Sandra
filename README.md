# Retail Data Engineering Pipeline

Este proyecto implementa un pipeline de Ingenieria de Datos (ETL) robusto diseñado para un escenario de Retail. El objetivo principal es la consolidacion de fuentes de datos heterogeneas, la aplicacion de tecnicas de limpieza profunda y la generacion de hallazgos analiticos mediante Reduccion de Dimensionalidad (PCA).

## Tecnologias Utilizadas
* Lenguaje: Python 3.14
* Librerias de Datos: Pandas, NumPy, PyArrow (Formato Parquet)
* Gestion de Bases de Datos: SQLite3
* Analitica Avanzada: Scikit-Learn (StandardScaler, PCA)
* Visualizacion: Plotly (Sankey Diagram interactivo), Seaborn, Matplotlib

## Estructura del Proyecto
```text
├── fuentes/               # Datos crudos en formatos SQL, JSON, CSV, TXT, XML, XLSX
├── scripts/
│   ├── preparar_datos.py  # Inicializador del entorno y generador de datasets sinteticos
│   └── visualizaciones.py # Generador de reportes graficos y diagramas
├── salidas/               # Artefactos procesados (Parquet), datasets finales y graficas
├── main_pipeline.py       # Script central encargado del proceso ETL y Analitica
└── README.md              # Documentacion del proyecto
