from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')



def cadastro_produto(request):

    msg = ''

    if request.method == "POST":

        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        descrição = request.POST.get('descrição')
        quantidade = request.POST.get('quantidade')

        Produto(nome=nome, valor=valor,
        descrição=descrição, quantidade=quantidade).save()

        msg = 'Produto Cadastrado!'

    return render(request, 'cadastro.html', {'msg': msg})


def consulta_produto(request):
    produto = Produto.objects.all()
    quantidade = 0
    for d in produto:
        quantidade = float(d.quantidade) + quantidade

    return render(request,'consulta.html', {'produto': produto, 'quantidade': quantidade})