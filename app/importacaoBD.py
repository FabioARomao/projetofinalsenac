import psycopg2 as SQL
#import sqlite3 as SQL
from . import criacaoBD as CBD

# Obtendo dados
def obtendoProdutos():
  
  # Cria uma conexão com BD e importa o arquivo de CB
  conexao = SQL.connect(CBD.arquivo)
  
  # Cria um cursor para BD
  cursor = conexao.cursor()
  
  # Seleciona todos os dados da tabela produtos
  cursor.execute("SELECT * FROM produtos")
  
  # Extrair os dados da tabela
  dados = cursor.fetchall()
  
  # Criação para exportação da Base
  base = []
  
  # Adiciona os registro na nossa base
  for registro in dados:
    dado = {
      'ID'        : registro[0],
      'Nome'      : registro[1],
      'Preço'     : registro[2],
      'Quantidade': registro[3],
      'Descrição' : registro[4]
    }
    base.append(dado)

  # Fecha a conexao
  conexao.close()

  return base
