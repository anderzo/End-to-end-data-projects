# Este proyecto implementa un flujo completo de datos, desde la ingesta y transformación hasta la visualización final en Power BI, con prácticas de ETL y modelado de datos.

- Se utilizaron múltiples archivos CSV como fuentes de datos.

- Los datos fueron cargados en Python utilizando pandas.

- Se validó la estructura inicial y la consistencia de los datos.

# Se realizó un análisis exploratorio (EDA) para identificar:

valores nulos
tipos de datos incorrectos
inconsistencias de formato

# Se limpiaron y normalizaron los datos:
conversión de tipos
estandarización de campos
preparación de claves para relaciones

# Se generaron archivos XLSX con los datos limpios.
capa para análisis exploratorio
uso en Excel o Looker Studio
Los XLSX no son la fuente oficial, solo una copia para análisis y validación.

# Los datos fueron cargados a PostgreSQL directamente desde los DataFrames limpios usando Python.

No se utilizaron archivos XLSX como fuente para la base de datos se hicieron desde los dataframes creados
Cargué datos mediante procesos ETL desde Python asegurando integridad referencial.

# Power BI se conectó directamente con la BD relacional.

El modelo relacional fue consumido para construir un dashboard interactivo.
Se desarrollaron KPIs y visualizaciones para:
ventas
clientes
tickets
stock
análisis por categoría, región y método de pago