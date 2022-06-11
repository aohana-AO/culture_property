# Generated by Django 4.0.5 on 2022-06-09 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_name_bunka_名称'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bunka',
            old_name='url',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='bunka',
            old_name='juusyo',
            new_name='愛媛県松山市住所',
        ),
        migrations.RenameField(
            model_name='bunka',
            old_name='bunnrui',
            new_name='文化財分類',
        ),
        migrations.RenameField(
            model_name='bunka',
            old_name='syurui',
            new_name='種類',
        ),
        migrations.RenameField(
            model_name='bunka',
            old_name='keido',
            new_name='経度',
        ),
        migrations.RenameField(
            model_name='bunka',
            old_name='ido',
            new_name='緯度',
        ),
    ]
