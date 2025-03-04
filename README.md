# deduplicator
# Processador de Planilhas ODS

Este projeto é um script em Python que processa arquivos **ODS** (Open Document Spreadsheet) para remover duplicatas e salvar um novo arquivo de planilha com dados únicos. O script carrega um arquivo `.ods`, extrai seus dados, remove duplicatas e cria um novo arquivo ODS com as informações filtradas.

## Funcionalidades

1. **Leitura de Arquivo ODS**: Carrega um arquivo de planilha ODS existente.
2. **Extração de Dados**: Extrai os dados da planilha linha por linha.
3. **Remoção de Duplicatas**: Filtra as linhas duplicadas com base no conteúdo das células.
4. **Criação de Novo Arquivo ODS**: Cria uma nova planilha ODS a partir dos dados únicos extraídos.
5. **Template de Planilha**: A possibilidade de usar um modelo ODS para criar o novo arquivo.

## Requisitos

- Python 3.x
- Biblioteca `odfpy` para manipulação de arquivos ODS.

Para instalar a biblioteca necessária, execute:

```bash
pip install odfpy
```

## Como Usar

1. Coloque o arquivo ODS de entrada (por exemplo, `sua_planilha.ods`) na mesma pasta que o script ou forneça o caminho completo para o arquivo.
2. (Opcional) Se você quiser usar um template para o novo arquivo ODS, forneça um arquivo de modelo (por exemplo, `template.ods`).
3. Execute o script para gerar um novo arquivo ODS sem duplicatas.

### Exemplo de Execução:

```bash
python remove_duplicatas_ods.py
```

Após a execução, o script salvará a planilha processada com dados únicos no arquivo `planilha_sem_duplicatas.ods`.

## Como Funciona o Código

1. **Carregar o Arquivo ODS**: O arquivo ODS de entrada é carregado usando a função `load()` da biblioteca `odf.opendocument`.
   
   ```python
   doc = load("sua_planilha.ods")
   sheets = doc.getElementsByType(Table)
   ```

2. **Extrair Dados da Planilha**: O código percorre todas as linhas (`TableRow`) da primeira planilha e extrai os dados de cada célula (`TableCell`).

   ```python
   rows = sheet.getElementsByType(TableRow)
   dados = []
   for row in rows:
       cells = row.getElementsByType(TableCell)
       dados.append([cell.firstChild.data if cell.firstChild else '' for cell in cells])
   ```

3. **Remover Duplicatas**: As linhas são filtradas para garantir que apenas dados únicos sejam mantidos. Isso é feito verificando se uma linha já está presente na lista `dados_unicos`.

   ```python
   dados_unicos = []
   for row in dados:
       if row not in dados_unicos:
           dados_unicos.append(row)
   ```

4. **Criar Novo Arquivo ODS**: A partir dos dados únicos, um novo arquivo ODS é criado. As linhas únicas são adicionadas à nova planilha e o arquivo é salvo.

   ```python
   new_doc = load("template.ods")  # Modelo de arquivo ODS, se necessário
   new_sheet = new_doc.getElementsByType(Table)[0]

   for row in dados_unicos:
       new_row = TableRow()
       for cell_value in row:
           new_cell = TableCell()
           new_cell.addText(cell_value)
           new_row.addElement(new_cell)
       new_sheet.addElement(new_row)

   new_doc.save("planilha_sem_duplicatas.ods")
   ```

5. **Salvar e Finalizar**: O novo arquivo ODS é salvo com o nome `planilha_sem_duplicatas.ods`.

   ```python
   new_doc.save("planilha_sem_duplicatas.ods")
   print("Planilha salva sem duplicatas.")
   ```

## Arquivos ODS

- **sua_planilha.ods**: Este é o arquivo de entrada que será processado.
- **template.ods** (Opcional): Um arquivo de template ODS que pode ser usado para criar a nova planilha com um formato pré-existente.
- **planilha_sem_duplicatas.ods**: O arquivo de saída, contendo os dados únicos.

## Exemplo de Entrada e Saída

### Exemplo de Planilha de Entrada (`sua_planilha.ods`):

| Nome  | Email               | Produto |
|-------|---------------------|---------|
| João  | joao@email.com       | Produto A |
| Maria | maria@email.com      | Produto B |
| João  | joao@email.com       | Produto A |
| Carla | carla@email.com      | Produto C |

### Exemplo de Planilha de Saída (`planilha_sem_duplicatas.ods`):

| Nome  | Email               | Produto |
|-------|---------------------|---------|
| João  | joao@email.com       | Produto A |
| Maria | maria@email.com      | Produto B |
| Carla | carla@email.com      | Produto C |

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para criar uma **issue** ou enviar um **pull request**.

## Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Este README fornece uma visão geral do funcionamento do script para processamento de planilhas ODS e como utilizá-lo para remover duplicatas.
