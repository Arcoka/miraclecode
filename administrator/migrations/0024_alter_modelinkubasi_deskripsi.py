# Generated by Django 5.1.5 on 2025-02-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0023_rename_token_team_modelinkubasi_token_modelinkubasi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelinkubasi',
            name='deskripsi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
