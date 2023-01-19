from django.forms import ModelForm
from cadastro.models import Pessoa


class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['primeiro_nome', 'ultimo_nome', 'email', 'numero_telefone']