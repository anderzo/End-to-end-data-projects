import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#unir tablas
folder = Path(__file__).parent
df_tienda_set = []

for js in folder.glob('*json'): 
    df = pd.read_json(js)
    df_tienda_set.append(df)

df_tienda_set_f = pd.concat(df_tienda_set, ignore_index= True) #esto lo une todo y lo pasa a DF

print('dimenciones: ', df_tienda_set_f.shape)
#print(df_tienda_set_f.columns)

df_tienda_set_f = df_tienda_set_f.drop(['dia_semana', 'mes', 'rango_edad', 'margen_beneficio'], axis =1)

print('dimenciones: ', df_tienda_set_f.shape)
#print(df_tienda_set_f.columns)

#hacer predicciones 
#1) difinir el modelo en entrenamiento y caracteristicas para las predicicones
# X = 'nombre_tienda', 'ciudad', 'producto','categoria','forma_pago', 'metodo_envio'
# y = 'total_final'

le_nombre_tienda = LabelEncoder()
le_ciudad = LabelEncoder()
le_producto = LabelEncoder()
le_categoria = LabelEncoder()
le_froma_de_pago = LabelEncoder()
le_metodo_envio = LabelEncoder()

df_tienda_set_f['tienda_id'] = le_nombre_tienda.fit_transform(df_tienda_set_f['nombre_tienda'])
df_tienda_set_f['ciudad_id'] = le_ciudad.fit_transform(df_tienda_set_f['ciudad'])
df_tienda_set_f['producto_id'] = le_producto.fit_transform(df_tienda_set_f['producto'])
df_tienda_set_f['categoria_id'] = le_categoria.fit_transform(df_tienda_set_f['categoria'])
df_tienda_set_f['forma_pago_id'] = le_froma_de_pago.fit_transform(df_tienda_set_f['forma_pago'])
df_tienda_set_f['metodo_envio_id'] = le_metodo_envio.fit_transform(df_tienda_set_f['metodo_envio'])

X = df_tienda_set_f[['tienda_id', 'ciudad_id', 'producto_id','categoria_id','forma_pago_id', 'metodo_envio_id']]
y = df_tienda_set_f['total_final']

print(df_tienda_set_f['tienda_id'].unique())

modelo = RandomForestRegressor()
modelo.fit(X, y)

df_nuevo = pd.DataFrame([{
    'nombre_tienda': 'Tienda Norte',
    'ciudad': 'Barcelona',
    'producto': 'Juego Sábanas',
    'categoria': 'Hogar',
    'forma_pago': 'Transferencia',
    'metodo_envio': 'Tienda'
}])

df_nuevo['tienda_id'] = le_nombre_tienda.transform(df_nuevo['nombre_tienda'])
df_nuevo['ciudad_id'] = le_ciudad.transform(df_nuevo['ciudad'])
df_nuevo['producto_id'] = le_producto.transform(df_nuevo['producto'])
df_nuevo['categoria_id'] = le_categoria.transform(df_nuevo['categoria'])
df_nuevo['forma_pago_id'] = le_froma_de_pago.transform(df_nuevo['forma_pago'])
df_nuevo['metodo_envio_id'] = le_metodo_envio.transform(df_nuevo['metodo_envio'])

X_nuevo = df_nuevo[['tienda_id', 'ciudad_id', 'producto_id','categoria_id', 'forma_pago_id', 'metodo_envio_id']]

prediccion = modelo.predict(X)
print(f"Las ventas estimandas para el presente mes: {prediccion[0]}")

df_tienda_set_f['predicciones'] = prediccion

print(df_tienda_set_f)

y_pred = modelo.predict(X)
print(mean_absolute_error(y, y_pred))

with pd.ExcelWriter('multiHojas.xlsx', engine='openpyxl') as writer:
    df_tienda_set_f.to_excel(writer, sheet_name='Ventas', index=False)

    df_nullos = pd.DataFrame({
        'nombre' : df_tienda_set_f.columns,
        'n_nulos': df_tienda_set_f.isnull().sum()
    })
    df_nullos.to_excel(writer, sheet_name='nullos', index=False)
