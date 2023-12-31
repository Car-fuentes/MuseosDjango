# Generated by Django 5.0 on 2023-12-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Museos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('museo', models.CharField(max_length=200)),
                ('descripción', models.TextField()),
                ('dirección', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
