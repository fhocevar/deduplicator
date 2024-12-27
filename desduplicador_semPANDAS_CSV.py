import csv

# Ler o arquivo CSV
with open('sua_planilha.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    dados = list(reader)

# Remover duplicatas
dados_unicos = []
for row in dados:
    if row not in dados_unicos:
        dados_unicos.append(row)

# Salvar em um novo arquivo CSV
with open('planilha_sem_duplicatas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dados_unicos)

print("Registros duplicados removidos com sucesso.")
