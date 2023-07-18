import sqlite3
import os

# Aponta o arquivo do Banco de Dados (BD)
arquivo = "database.db"

# Verifica se existe um banco de dados
if not(os.path.exists(arquivo)):

  # Cria uma conexão com BD
  conexao = sqlite3.connect(arquivo)

  # Cria a tabela de produtos
  conexao.execute("""
  CREATE TABLE produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    quantidade INTEGER,
    descricao TEXT
  )
  """)
  
  # Cria os registros no SQL
  produtos = [
    #Nome,  Preço, Quantidade, Descrição
    ('Caneta',5.00,100,"Caneta azul, azul caneta"),
    ('Laptop', 2999.99, 100, "Notebook da Xuxa em parceria com Positivo"),
    ('iPhone', 14999.99, 1000, "Celular mais caro do universo"),
    ('Galaxy S23', 5999.99, 500, "Celular que trava"),
    ('Televisão', 799.99, 10, 'Uma TV de alta definição com ampla variedade de recursos.'),
      ('Câmera digital', 399.99, 100, 'Uma câmera portátil para capturar fotos e vídeos.'),
      ('Fones de ouvido', 99.99, 50, 'Fones de ouvido sem fio com cancelamento de ruído.'),
      ('Relógio inteligente', 199.99, 20, 'Um relógio com recursos de monitoramento e notificações.'),
      ('Console de videogame', 499.99, 11, 'Um sistema de jogos para entretenimento.'),
      ('Tablet', 299.99, 29, 'Um dispositivo portátil para navegação e consumo de mídia.'),
      ('Impressora', 149.99, 25, 'Uma impressora para imprimir documentos e fotos.'),
      ('Monitor de computador', 199.99, 30, 'Um monitor de alta resolução para uso com computadores.'),
      ('Caixa de som Bluetooth', 79.99, 50, 'Uma caixa de som sem fio com conexão Bluetooth.'),
      ('Refrigerador', 1299.99, 21, 'Um refrigerador com recursos de armazenamento e refrigeração.'),
      ('Máquina de lavar roupa', 899.99, 10, 'Uma máquina para lavar roupas automaticamente.'),
      ('Aspirador de pó', 199.99, 11, 'Um dispositivo para limpar pisos e tapetes.'),
      ('Cafeteira', 59.99, 30, 'Uma máquina para fazer café.'),
      ('Panela elétrica', 89.99, 11, 'Uma panela para cozinhar alimentos de forma elétrica.'),
      ('Ferro de passar roupa', 39.99, 1, 'Um ferro para passar roupas e remover rugas.'),
      ('Liquidificador', 49.99, 5,'Um aparelho para misturar alimentos e fazer sucos.'),
      ('Secador de cabelo', 29.99, 10, 'Um dispositivo para secar cabelos com ar quente.'),
      ('Ventilador de teto', 99.99, 100, 'Um ventilador fixado no teto para circulação de ar.')
  ]

  # Inserir os dados na lista na tabela do SQL
  conexao.executemany("""
  INSERT INTO produtos (nome, preco, quantidade, descricao)
  VALUES (?,?,?,?)""", produtos)

  # Subir as alterações
  conexao.commit()

  # Fecha a conexão com SQL
  conexao.close()

  print("Feita a criação do BD")