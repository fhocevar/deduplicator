import pandas as pd

# Carregar o arquivo da planilha
# Pode ser um arquivo CSV, XLSX, etc.
# Exemplo para CSV: df = pd.read_csv('arquivo.csv')
# Exemplo para Excel: df = pd.read_excel('arquivo.xlsx')

# Supondo que seja um arquivo CSV
df = pd.read_csv('sua_planilha.csv')

# Remover registros duplicados
# A função drop_duplicates remove linhas duplicadas
df_sem_duplicatas = df.drop_duplicates()

# Salvar o novo arquivo sem duplicatas
# Pode salvar como CSV ou Excel
df_sem_duplicatas.to_csv('planilha_sem_duplicatas.csv', index=False)

# Ou, para Excel:
# df_sem_duplicatas.to_excel('planilha_sem_duplicatas.xlsx', index=False)

print("Registros duplicados foram removidos com sucesso.")
