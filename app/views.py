from django.shortcuts import render, redirect
from . import importacaoBD
from . import criacaoBD
from . import gerenciarBD
from django.contrib import messages
from django.contrib.auth import get_user, logout, authenticate, hashers, login, auth_login
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



class LoginForm(forms.Form):
   email = forms.Charfield()
   password = fprms.Charfield(widget= forms.PasswordInput)
   remember_me = forms.BoolenField()

def login(request):
  if request.method == 'GET':
    return render (request, 'login.html')


def login(request):
    if request.method == 'POST':
        form - LoginForm(request.POST)
        if form.is_valid():
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           remember_me =  form.cleaned_data['remember_me']
           user = authenticate(email=email, password=password)
           if user:
              login(request, user)
              if not remember_me:
                 request.session.set_expiry(0)

              return redirect('login.html')
    else:
        form = LoginForm()
        render(request, 'profile.html', {'form': form})
    

    con = criacaoBD.conecta_bd()
    cur = con.cursor()
    cur.execute("select email from logins where email=email;")
    user = cur.fetchone()
    print(user, password)
    cur.close()
    con.close()

def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html')


def signup(request):
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