from django.shortcuts import render, redirect
from cadastro.forms import PessoasModel
from cadastro.models import Pessoa

def home(request):
    data = {}
    data['db'] = Pessoa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = PessoasModel()
    return render(request, 'form.html', data)

def create(request):
    form = PessoasModel(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    data['form'] = PessoasModel(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data= {}
    data['db'] = Pessoa.objects.get(pk=pk)
    form = PessoasModel(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')