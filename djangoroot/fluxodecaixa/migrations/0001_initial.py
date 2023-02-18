# Generated by Django 4.0.8 on 2023-02-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relatorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FluxoDeCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('descricao', models.CharField(blank=True, max_length=90, null=True)),
                ('relatorios', models.ManyToManyField(to='relatorio.relatorio')),
            ],
        ),
    ]
