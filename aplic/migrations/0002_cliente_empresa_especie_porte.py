# Generated by Django 2.2.19 on 2022-12-05 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Animal')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('porte', models.CharField(blank=True, choices=[('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande')], max_length=100, verbose_name='Porte')),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.Animal')),
            ],
            options={
                'verbose_name': 'Porte',
                'verbose_name_plural': 'Portes',
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('porte', models.CharField(blank=True, choices=[('Cachorro', 'Cachorro'), ('Gato', 'Gato')], max_length=100, verbose_name='Porte')),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.Animal')),
            ],
            options={
                'verbose_name': 'Especie',
                'verbose_name_plural': 'Especies',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('clientes', models.ManyToManyField(to='aplic.Cliente')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
