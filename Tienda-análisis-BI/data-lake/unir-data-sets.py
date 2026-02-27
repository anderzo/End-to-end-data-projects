import pandas as pd
from pathlib import Path

folder = Path(__file__).parent

lista_df = []

for fl in folder.glob('*json'):
    df = pd.read_json(fl)
    lista_df.append(df)

df_final = pd.concat(lista_df, ignore_index=True)

print(df_final.shape)

