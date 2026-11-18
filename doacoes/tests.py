from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Doacao


class DoacaoModelTest(TestCase):

    def test_criar_doacao_com_dados_validos(self):
        doacao = Doacao.objects.create(
            responsavel='Maria',
            material='Livros',
            quantidade=Decimal('2.00'),
            unidade='unidades'
        )

        self.assertEqual(Doacao.objects.count(), 1)
        self.assertEqual(doacao.material, 'Livros')

    def test_representacao_da_doacao(self):
        doacao = Doacao(
            responsavel='Maria',
            material='Livros',
            quantidade=Decimal('2.00'),
            unidade='unidades'
        )

        self.assertEqual(str(doacao), 'Livros - Maria')

    def test_quantidade_menor_que_minimo_e_invalida(self):
        doacao = Doacao(
            responsavel='Maria',
            material='Livros',
            quantidade=Decimal('0.00'),
            unidade='unidades'
        )

        with self.assertRaises(ValidationError):
            doacao.full_clean()