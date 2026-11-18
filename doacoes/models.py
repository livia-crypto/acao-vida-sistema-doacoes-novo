
from django.db import models
from django.core.validators import MinValueValidator

class Doacao(models.Model):

    TIPOS_MATERIAL = [
        ('Roupas', 'Roupas'),
        ('Livros', 'Livros'),
        ('Alimentos', 'Alimentos'),
        ('Recicláveis', 'Recicláveis'),
        ('Outros', 'Outros'),
    ]

    UNIDADES = [
        ('kg', 'Quilogramas (kg)'),
        ('unidades', 'Unidades'),
    ]

    responsavel = models.CharField(
        max_length=100,
        verbose_name='Responsável'
    )

    material = models.CharField(
        max_length=30,
        choices=TIPOS_MATERIAL,
        verbose_name='Tipo de material'
    )

    quantidade = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name='Quantidade'
    )

    unidade = models.CharField(
        max_length=10,
        choices=UNIDADES,
        verbose_name='Unidade de medida'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do cadastro'
    )

    def __str__(self):
        return f'{self.material} - {self.responsavel}'

    class Meta:
        ordering = ['-data_cadastro']
        