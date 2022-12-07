from django.contrib import admin

from .models import Animal, Porte, Cliente, Especie, Empresa
# Register your models here.

#curso
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome',)

#professor
@admin.register(Porte)
class PorteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porte', 'animal')

#aluno
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco', 'telefone', 'email', 'animal')

#disciplina
@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('animal', 'nome', 'porte')

#turma
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

