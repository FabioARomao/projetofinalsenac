from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas', views.pessoas, name='pessoas'),
    path('produtos', views.produtos, name='produtos'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('atualizar/<int:item_id>', views.atualizar, name='atualizar'),
    path('remove/<int:item_id>', views.remove, name='remove')
]
