import psycopg2 as SQL
#import sqlite3 as SQL
#from . import criacaoBD
import criacaoBD

# Obtendo dados
def obtendoProdutos(sql):
  
  # Cria uma conexão com BD e importa o arquivo de CB
  conexao = SQL.connect(criacaoBD.conecta_bd(sql))
  print(conexao)
  
  # Cria um cursor para BD
  cur = conexao.cursor()
  
  # Seleciona todos os dados da tabela produtos
  sql = '''SELECT * FROM app_produto'''
  cur.execute(sql)
  
  # Extrair os dados da tabela
  dados = cur.fetchall()
  
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
    print(dado)

  # Fecha a conexao
  conexao.close()

  print(base)
