import xlrd
import xlwt

# Carregar o arquivo .xls
wb = xlrd.open_workbook('empresas_multicidades_moçambique.xls')
sheet = wb.sheet_by_index(0)

# Extrair dados da planilha
dados = []
for row in range(sheet.nrows):
    dados.append(sheet.row_values(row))

# Remover duplicatas
dados_unicos = []
for row in dados:
    if row not in dados_unicos:
        dados_unicos.append(row)

# Criar uma nova planilha para salvar os dados únicos
new_wb = xlwt.Workbook()
new_sheet = new_wb.add_sheet('Sheet1')

# Escrever os dados únicos
for i, row in enumerate(dados_unicos):
    for j, cell in enumerate(row):
        new_sheet.write(i, j, cell)

# Salvar a nova planilha
new_wb.save('moçambique_sem_duplicatas.xls')
print("Registros duplicados foram removidos com sucesso.")
