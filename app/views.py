from django.shortcuts import render, redirect
from . import importacaoBD
from . import criacaoBD
from . import gerenciarBD
from . import leitura
from django.http import JsonResponse
from django.contrib import messages, auth
from django.contrib.auth import get_user, logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import psycopg2
import os



def index(request):
    return render (request, 'index.html')

def remove(request, item_id):
        # Cria uma conexão com BD e importa o arquivo de CBD
        conexao = psycopg2.connect(criacaoBD.arquivo)
        
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
  devolver1 = {'itens': dados1}
  return render(request, 'pessoas.html', devolver1)

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
    return render(request, 'profile.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def callback(request):

    return nomes
    #language = request.args.get('language')
    #return '''<h1>{}</h1>'''.format(language)

nomes = leitura.leitura_de_arquivo("babys.json")

def login(request):
    if (request.method == 'POST'):
          email = request.POST['email']
          password = request.POST['password']
          if not email.strip():
            print("Email nao pode ficar vazio")
            return redirect ('login')
          if not password.strip():
              print("Senha nao pode ficar vazio")
              return redirect ('login')
          print(email, password)
          if User.objects.filter(email=email).exists():
             nome = User.objects.filter(email=email).values_list('username', flat=True).get
             user = auth.authenticate(request, username=nome, password=password)
             if user is not None:
                auth.login(request, user)
                print('Login Realizado com Sucesso!!!')
                return redirect('dashboard') 
          return redirect('profile')
    return render (request, 'login.html')

def signup(request):
  if (request.method == 'POST'):
      email = request.POST['email']
      if not email.strip():
        print("Email nao pode ficar vazio")
        return render (request, 'signup.html')
      username = request.POST['name']
      if not username.strip():
        print("Nome nao pode ficar vazio")
        return render (request, 'signup.html')
      password = request.POST['password']
      if not password.strip():
        print("Senha nao pode ficar vazio")
        return render (request, 'signup.html')

      if User.objects.filter(username=username, email=email).exists():
        print("Usuario ja possui cadastro!!")
        return render (request, 'signup.html')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Usuario cadastrado com sucesso!!!")
        return render (request, 'login.html')
    
  else:
    return render(request, 'signup.html')
  

@login_required
def logout(request):
    auth.logout(request)
    return redirect ('login')
