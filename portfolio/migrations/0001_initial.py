# Generated by Django 4.2.7 on 2023-12-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoWebAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('imagem', models.CharField(max_length=150)),
            ],
        ),
    ]