from odf.opendocument import load
from odf.table import Table, TableRow, TableCell

# Carregar o arquivo .ods
doc = load("sua_planilha.ods")
sheets = doc.getElementsByType(Table)

# Supondo que você tenha uma única planilha
sheet = sheets[0]
rows = sheet.getElementsByType(TableRow)

# Extrair dados da planilha
dados = []
for row in rows:
    cells = row.getElementsByType(TableCell)
    dados.append([cell.firstChild.data if cell.firstChild else '' for cell in cells])

# Remover duplicatas
dados_unicos = []
for row in dados:
    if row not in dados_unicos:
        dados_unicos.append(row)

# Criar um novo documento ODS com dados únicos
from odf.table import TableColumn
new_doc = load("template.ods")  # Modelo de arquivo ODS, se necessário
new_sheet = new_doc.getElementsByType(Table)[0]

for row in dados_unicos:
    new_row = TableRow()
    for cell_value in row:
        new_cell = TableCell()
        new_cell.addText(cell_value)
        new_row.addElement(new_cell)
    new_sheet.addElement(new_row)

# Salvar o novo arquivo ODS
new_doc.save("planilha_sem_duplicatas.ods")
print("Planilha salva sem duplicatas.")
