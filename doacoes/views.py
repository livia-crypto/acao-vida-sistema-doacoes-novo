
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import DoacaoForm
from .models import Doacao

def inicio(request):
    return render(request, 'doacoes/inicio.html')

def cadastrar_doacao(request):

    if request.method == 'POST':
        form = DoacaoForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Doação cadastrada com sucesso!'
            )

            return redirect('historico')

    else:
        form = DoacaoForm()

    return render(
        request,
        'doacoes/cadastro.html',
        {'form': form}
    )

def historico(request):

    doacoes = Doacao.objects.all()

    total_doacoes = doacoes.count()

    return render(
        request,
        'doacoes/historico.html',
        {
            'doacoes': doacoes,
            'total_doacoes': total_doacoes,
        }
    )