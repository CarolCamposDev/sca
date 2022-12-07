from django.db import models
from stdimage.models import StdImageField
import uuid


# Create your models here.

#Curso
class Animal(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)

    facebook = models.CharField('Facebook', blank=True, max_length=200)
    linkedin = models.CharField('LinkedIn', blank=True, max_length=200)
    twitter = models.CharField('Twitter', blank=True, max_length=200)
    instagram = models.CharField('Instagram', blank=True, max_length=200)

    class Meta:
        abstract = True
        verbose_name = 'Porte'
        verbose_name_plural = 'Portes'

    def __str__(self):
        return self.nome

    def get_file_path(_instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return filename


#professor
class Porte(Pessoa):
    OPCOES = (
        ('Pequeno',       'Pequeno'),
        ('Médio',        'Médio'),
        ('Grande',  'Grande'),
    )
    porte = models.CharField('Porte', blank=True, max_length=100, choices=OPCOES)
    animal = models.ForeignKey(Animal, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Porte'
        verbose_name_plural = 'Portes'

#aluno
class Cliente(Pessoa):
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail', blank=True, max_length=200)
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

#disciplina
class Especie(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    OPCOES = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
    )
    porte = models.CharField('Porte', blank=True, max_length=100, choices=OPCOES)
    animal = models.ForeignKey(Animal, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.nome


#turma
class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.IntegerField('Telefone')
    clientes = models.ManyToManyField(Cliente)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f"{self.nome} / {self.endereco} / {self.telefone} / {self.clientes}"

