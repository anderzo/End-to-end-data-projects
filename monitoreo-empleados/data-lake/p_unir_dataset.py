import pandas as pd
from pathlib import Path

#folder = Path(__file__).parent #si vamos a ejecutar desde otras ubicaciones
folder = Path('.') #carpeta donde ejecutas el script

dfs=[]

for archivo in folder.glob('*.txt'):
    df=pd.read_csv(archivo, sep=",")
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index= True)

print('Guradado exitoso')
print(df_final.describe)
print(df_final.dtypes)
print(df_final.columns)
print(df_final.shape)
df_final.to_excel('e_unido.xlsx', index = False, sheet_name = 'hoja_1')
