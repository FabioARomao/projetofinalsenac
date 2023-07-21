#import psycopg2
#import criacaoBD
#
##Cria uma conexao com banco de dados
#def __abrirConexao__(comando, args):
#  #conexao com o bd
#  conexao = criacaoBD.connect()
#  print(conexao)
#
#  #criando um cursor
#  cursor = conexao.cursor()
#
#  #executar comando no psycopg2
#  cursor.execute(comando, args)
#
#  #obter resultado do comando
#  resultado = cursor.fetchall()
#  
#  #grava no banco
#  conexao.commit()
#
#  #fechando conexao com banco
#  conexao.close()
#
#  #return resultado
#  print(resultado)
#
##Atualiza um item do banco de dados
#def atualizar(id, nome, preco, quantidade, descricao):
#  __abrirConexao__(
#  """
#  update produtos set nome = ?, preco = ?, quantidade = ?, descricao = ? where id = ?
#  """,
#  (nome, preco, quantidade, descricao, id)
#    
#  )
#
#def atualizar_pessoa(id, nome, sobrenome, cpf, endereco):
#  __abrirConexao__(
#  """
#  update pessoas set nome = ?, sobrenome = ?, cpf = ?, endereco  = ? where id = ?
#  """,
#  (nome, sobrenome, cpf, endereco, id)
#    
#  )
#
## adiciona um item no banco de dados
#def adicionar(nome, preco, quantidade, descricao):
#  __abrirConexao__(
#  """
#  insert into produtos (nome, preco, quantidade, descricao) values (?,?,?,?)
#  """,
#    (nome, preco, quantidade, descricao)
#    
#  )
#
#def adicionar_pessoa(nome, sobrenome, cpf, endereco):
#  __abrirConexao__(
#  """
#  insert into produtos (nome, sobrenome, cpf, endereco) values (?,?,?,?)
#  """,
#    (nome, sobrenome, cpf, endereco)
#    
#  )