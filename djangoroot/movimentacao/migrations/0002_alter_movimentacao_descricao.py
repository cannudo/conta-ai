# Generated by Django 4.0.8 on 2023-02-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='descricao',
            field=models.TextField(max_length=140, null=True),
        ),
    ]