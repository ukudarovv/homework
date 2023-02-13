# Generated by Django 4.1.6 on 2023-02-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Ребенок',
                'verbose_name_plural': 'Дети',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('children', models.ManyToManyField(to='family.child')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
    ]
