
from django import forms
from .models import Doacao

class DoacaoForm(forms.ModelForm):

    class Meta:
        model = Doacao

        fields = [
            'responsavel',
            'material',
            'quantidade',
            'unidade',
        ]

        widgets = {
            'responsavel': forms.TextInput(
                attrs={
                    'placeholder': 'Digite o nome do responsável'
                }
            ),

            'quantidade': forms.NumberInput(
                attrs={
                    'placeholder': 'Ex.: 5',
                    'min': '0.01',
                    'step': '0.01'
                }
            ),
        }

        labels = {
            'responsavel': 'Nome do responsável',
            'material': 'Tipo de material',
            'quantidade': 'Quantidade',
            'unidade': 'Unidade de medida',
        }
        