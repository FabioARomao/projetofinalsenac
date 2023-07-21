from django.shortcuts import render, redirect
from . import importacaoBD
from . import criacaoBD
from . import gerenciarBD
from django.contrib import messages
from django.contrib.auth import get_user, logout, authenticate, hashers
from django.contrib.auth.decorators import login_required
import sqlite3
import psycopg2
import os
from . import leitura


def index(request):
    return render (request, 'index.html')

def remove(request, item_id):
        # Cria uma conexão com BD e importa o arquivo de CBD
        conexao = sqlite3.connect(criacaoBD.arquivo)
        
        # Criar um cursor
        cursor = conexao.cursor()
        
        # Executando a remoção no BD
        cursor.execute("""
          DELETE FROM pessoas where id = ?
        """, (item_id,))
        
        #Subindo as alterações realizadas no BD
        conexao.commit()
        
        # Fechando a conexão com o BD
        conexao.close()

        # Atualizar a tela
        dados = importacaoBD.obtendoProdutos()
        devolver = {'itens': dados}
        return render(request, 'index.html', devolver)

        #dados1 = importacaoBD.obtendoPessoas()
        #devolver = {'itens': dados1}
        #return render(request, 'index.html', devolver)
        # Removendo todos os itens
        # cursor.execute("DELETE FROM produtos")

# Create your views here.
def produtos(request):
  dados = importacaoBD.obtendoProdutos()
  devolver = {'itens': dados}
  return render(request, 'produtos.html', devolver)

def pessoas(request):
  dados1 = importacaoBD.obtendoPessoas()
  devolver = {'itens': dados1}
  return render(request, 'pessoas.html', devolver)

def pratos(request, argumento):
  return render(request, 'pratos.html', {
    'prato': argumento,
    'descricao': """
    dklfklczbnbfmdbjkfbkfjksbankfjkba
    smjbfjkbfkbafjkka
    """,
    'imagem':argumento
  })


def adicionar(request):
  #vamos usar o post
  if request.method == "POST":
    try:
      preco = float(request.POST['preco'])
      quantidade = int(request.POST['quantidade'])
    except Exception:
      messages.error(request, "Digite um valor valido")
      return redirect('adicionar')

    nome = request.POST['nome']
    descricao = request.POST['descricao']

    gerenciarBD.adicionar(nome, preco, quantidade, descricao)
    return redirect('index')
  return render(request, 'gerenciar.html', {'titulo': 'Adicionar'})


def atualizar(request, item_id):
  #vamos usar o post
  if request.method == "POST":
    try:
      preco = float(request.POST['preco'])
      quantidade = int(request.POST['quantidade'])
    except Exception:
      messages.error(request, "Digite um valor valido")
      return redirect('atualizar')

    nome = request.POST['nome']
    descricao = request.POST['descricao']

    gerenciarBD.atualizar(item_id, nome, preco, quantidade, descricao)
    return redirect('index')
  return render(request, 'gerenciar.html', {'titulo': 'Atualizar'})




#def get_db_connection():
#    conn = psycopg2.connect(host='localhost',
#                            database='auth',
#                            port=5438,
#                            user=os.environ['DB_USERNAME'],
#                            password=os.environ['DB_PASSWORD'])
#    return conn


#def index():
#    conn = get_db_connection()
#    conn.close()
#    return render_template('index.html')
#    #return 'Index'

@login_required
def profile(request):
    return render(request, 'profile.html', name=get_user.name)


@login_required
def dashboard(request):
    return render (request, 'dashboard.html', name=get_user.name)

@login_required
def callback(request):

    return nomes
    #language = request.args.get('language')
    #return '''<h1>{}</h1>'''.format(language)

nomes = leitura.leitura_de_arquivo("babys.json")



def login(request, methods=(['GET'])):
  if request.method == 'GET':
    return render (request, 'login.html')


def login_post(request, methods=(['POST'])):
    if request.method == 'POST':
        login(user, remember=remember)
        return render (request, 'login.html')
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
    

    #con = get_db_connection()
    #cur = con.cursor()
    #cur.execute("select email from logins where email=email;")
    #user = cur.fetchone()
    #print(user, password)
    #cur.close()
    #con.close()
    
    if not user or not hashers(user, password):
        return redirect(url_for('profile'))
    login_user(user, remember=remember)
    return redirect(url_for('profile'))
    

def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html')


def signup_post(request):
    if request.method == 'POST':
      return render (request, 'login.html')
      name = request.form['name']
      email = request.form['email']
      password = request.form['password']

      con = get_db_connection()
      cur = con.cursor()
      cur.execute('insert into logins (email, name, password)' 'values(%s, %s, %s)', (email, name, password))
      cur.close()
      con.close()
    
      return render (request, 'login.html')
    
    if email:
        messages('Email ja esta registrado', 'success')
        return render (request, 'signup.html')
    
    #create a new user
    new_user = cur.cursor(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    #add the user to database
    cur.session.add(new_user)
    cur.session.commit()
    



@login_required
def logouts(request):
    logout()
    return redirect(url_for('login'))


def usuario(request):
    if(request.method == 'GET'):
        #lista = User.query.filter_by(email='fabio@fabio.com.br').first()
        #if lista:
        #    print(lista)
        #    return str(lista)
        #else:
        #    return str('nao possui usuario cadastrado')

        data = [{
            "Modules" : 16,
            "Subject" : "estrutura de dados e algoritmos 1",
        },
        {
            "Modules" : 17,
            "Subject" : "estrutura de dados e algoritmos 2",
        }]
        return jsonify(data)