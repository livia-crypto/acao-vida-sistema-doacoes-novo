
from django.contrib import admin
from .models import Doacao

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):

    list_display = (
        'responsavel',
        'material',
        'quantidade',
        'unidade',
        'data_cadastro',
    )

    list_filter = (
        'material',
        'unidade',
    )

    search_fields = (
        'responsavel',
        'material',
    )