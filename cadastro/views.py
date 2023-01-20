from django.shortcuts import render, redirect
from cadastro.forms import PessoasForm
from cadastro.models import Pessoa

def home(request):
    data = {}
    # Pessoa.objects.all = Pegar todos os dados e inserir no dicionário 'data'.
    data['db'] = Pessoa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    # Recebe o formulário de PessoasForm()
    data['form'] = PessoasForm()
    return render(request, 'form.html', data)

def create(request):
    # request.POST = Dados do formulário
    form = PessoasForm(request.POST or None)
    if form.is_valid():
        # Salvar no banco da dados
        form.save()
        # Redirecionar p/ a pagina principal
        return redirect('home')

def view(request, pk):
    data = {}
    # Pessoa.object.get(pk=pk) = Pegar os dados pela primer key e inserir no dicionário.
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    # Recebendo os dados de Pessoa de acordo com a pk
    data['db'] = Pessoa.objects.get(pk=pk)
    # Recebendo os formulário
    data['form'] = PessoasForm(instance=data['db']) # Instance será a pessoa de acordo com a PK.
    return render(request, 'form.html', data)

def update(request, pk):
    data= {}
    # Recebendo os dados de Pessoa de acordo com a pk
    data['db'] = Pessoa.objects.get(pk=pk)
    # Recebendo os formulário
    form = PessoasForm(request.POST or None, instance=data['db']) # Django vai pegar os dados em request.POST em instance=data['db]
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    # Deletando
    db.delete()
    return redirect('home')