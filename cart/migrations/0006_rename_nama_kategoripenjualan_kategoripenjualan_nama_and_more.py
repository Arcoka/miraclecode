# Generated by Django 5.1.5 on 2025-05-09 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_rename_token_jasa_token_jasa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategoripenjualan',
            old_name='nama_kategoripenjualan',
            new_name='nama',
        ),
        migrations.RemoveField(
            model_name='kategoripenjualan',
            name='deskripsi_kategoripenjualan',
        ),
    ]
