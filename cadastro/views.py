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