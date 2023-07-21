import psycopg2

def conecta_bd():
    conexao = psycopg2.connect(host='0.0.0.0',
                            database='auth',
                            port=5432,
                            user='postgres',
                            password='postgres')
    return conexao

def criar_tabela(sql):
    conexao = conecta_bd()
    cur = conexao.cursor()
    try:
        cur.execute(sql)
        conexao.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conexao.rollback()
        cur.close()
        return 1
    cur.close()

sql = '''CREATE TABLE public.pessoas(
      id SERIAL PRIMARY KEY,
      nome TEXT,
      sobrenome TEXT,
      cpf INTEGER,
      endereco TEXT,
      criado DATE
    )'''

criar_tabela(sql)

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

def inserir_db(sql):
    conexao = conecta_bd()
    cur = conexao.cursor()
    try:
        cur.execute(sql)
        conexao.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conexao.rollback()
        cur.close()
        return 1
    cur.close()

#Atualiza um item do banco de dados
def atualizar(id, nome, preco, quantidade, descricao):
  conecta_bd(
  """
  update produtos set nome = ?, preco = ?, quantidade = ?, descricao = ? where id = ?
  """,
  (nome, preco, quantidade, descricao, id)
    
  )

def atualizar_pessoa(id, nome, sobrenome, cpf, endereco):
  conecta_bd(
  """
  update pessoas set nome = ?, sobrenome = ?, cpf = ?, endereco  = ? where id = ?
  """,
  (nome, sobrenome, cpf, endereco, id)
    
  )

# adiciona um item no banco de dados
def adicionar(nome, preco, quantidade, descricao):
  conecta_bd(
  """
  insert into produtos (nome, preco, quantidade, descricao) values (?,?,?,?)
  """,
    (nome, preco, quantidade, descricao)
    
  )

def adicionar_pessoa(nome, sobrenome, cpf, endereco):
  conecta_bd(
  """
  insert into produtos (nome, sobrenome, cpf, endereco) values (?,?,?,?)
  """,
    (nome, sobrenome, cpf, endereco)
    
  )