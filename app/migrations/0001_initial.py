# Generated by Django 4.0.5 on 2022-06-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, verbose_name='username')),
                ('age', models.IntegerField(max_length=3, verbose_name='age')),
                ('sex', models.CharField(max_length=6, verbose_name='sex')),
            ],
        ),
    ]
