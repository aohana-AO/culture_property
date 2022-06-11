# Generated by Django 4.0.5 on 2022-06-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bunka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=20, verbose_name='番号')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('ido', models.CharField(max_length=20, verbose_name='緯度')),
                ('keido', models.CharField(max_length=20, verbose_name='経度')),
                ('bunnrui', models.CharField(max_length=20, verbose_name='文化財分類')),
                ('syurui', models.CharField(max_length=20, verbose_name='種類')),
                ('juusyo', models.CharField(max_length=20, verbose_name='愛媛県松山市住所')),
                ('url', models.CharField(max_length=20, verbose_name='URL')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, verbose_name='username'),
        ),
    ]
