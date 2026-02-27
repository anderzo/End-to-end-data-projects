# Proyecto de Análisis y Predicción de Riesgo Crediticio

- Python · Pandas ·  Power BI
- Desarrollé un pipeline completo de datos desde ingesta y limpieza hasta visualización ejecutiva.
- Integré resultados del modelo en Power BI para análisis interactivo.

# Limpieza y Preparación de Datos

- Identificación y tratamiento de valores nulos y datos inconsistentes.
- Conversión de campos numéricos almacenados como texto (moneda, separadores, “K”, etc.).
- Normalización de variables categóricas (género, estado civil, educación).
Corrección de tipos de datos (string → float / int).
Imputación de valores faltantes utilizando medidas estadísticas (moda).
Exportación de datasets limpios a XLSX para su consumo en herramientas de BI.

# Construcción de dashboards en Power BI a partir de los datos procesados en Python.

Creación de KPIs clave: clientes en mora, clientes al día, total de clientes y precisión del modelo.
Implementación de segmentadores por edad, salario, género, educación y tipo de tarjeta.
Integración de predicciones del modelo ML dentro del dashboard.
Uso de HTML Content para personalización visual de tarjetas KPI
Implementé tarjetas personalizadas con HTML Content.
Analicé riesgo crediticio por edad, salario, educación y comportamiento transaccional

# El repositorio está estructurado de forma modular para facilitar mantenimiento y escalabilidad:

data-lake: datos crudos
data-sets: datasets limpios
EDA: scripts de limpieza y análisis exploratorio
ML: modelos de Machine Learning y predicciones

dashboard: dashboards desarrollados en distintas herramientas
