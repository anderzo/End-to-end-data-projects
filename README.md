# End-to-end-data-projects
Repositorio de proyectos de análisis de datos, ingeniería de datos, BI y modelado de datos ML

## Estructura general de cada proyecto
Cada proyecto dentro del repositorio cuenta con las siguientes carpetas:

## data-lake/
Almacena los datos crudos obtenidos de APIs, archivos planos (JSON, CSV, TXT, etc.) u otras fuentes.

No se modifican: sirven como respaldo y punto de partida.
## EDA/
- Contiene los scripts en Python (.py) o notebooks (.ipynb) usados para:
- Exploratory Data Analysis
- Limpieza y transformación de datos (ETL)
- Validaciones y preparación para carga

## data-sets/
- Guarda copias de los datos limpios, ya sea en:
- Archivos xlsx (para análisis en Excel, tablas dinámicas o Looker Studio), csv, json, txt , otros
- Exportaciones desde base de datos, según el proyecto
  
## dashboards/
- Incluye los productos finales de visualización:
- Archivo original (.pbix, Looker, etc.)
- Capturas del dashboard
- Reportes visuales listos para presentación

## ML/ (si aplica)
- Contiene modelos de Machine Learning, incluyendo:
- Scripts de entrenamiento
- Evaluación
- Features utilizadas
  
## requirements.txt
Lista las librerías de Python necesarias para reproducir el proyecto.
