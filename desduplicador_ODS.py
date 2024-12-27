import pandas as pd

# Carregar o arquivo ODS
# Para carregar arquivos ODS, usamos o parâmetro 'odf' ao invés de 'excel'
df = pd.read_excel('sua_planilha.ods', engine='odf')

# Remover registros duplicados
df_sem_duplicatas = df.drop_duplicates()

# Salvar a planilha sem duplicatas de volta no formato ODS
# O pandas não suporta salvar diretamente em ODS, mas você pode salvar como Excel
df_sem_duplicatas.to_excel('planilha_sem_duplicatas.xlsx', index=False)

# Caso queira salvar em CSV, também é uma opção
# df_sem_duplicatas.to_csv('planilha_sem_duplicatas.csv', index=False)

print("Registros duplicados foram removidos e a planilha foi salva.")
