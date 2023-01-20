from django.forms import ModelForm
from cadastro.models import Pessoa

# Criando os formulários
class PessoasForm(ModelForm):
    class Meta:
        model = Pessoa
        # Campos que serão exibidos
        fields = ['primeiro_nome', 'ultimo_nome', 'email', 'numero_telefone']