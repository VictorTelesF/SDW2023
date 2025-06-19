import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('anime_lista.csv')

# Ordenar pelo ano de lançamento (ajuste o nome da coluna conforme necessário)
df_ordenado = df.sort_values(by="Ano de Lançamento", ascending=True)
df_order = df.sort_values(by="Nome", ascending=True)

# Salvar o resultado em um novo arquivo CSV
df_ordenado.to_csv('anime_lista_ordenado_por_ano.csv', index=False)
df_order.to_csv('anime_lista_ordenado_por_nome.csv', index=False)