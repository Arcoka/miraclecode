# Generated by Django 5.1.5 on 2025-04-17 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0032_team_facebook_team_instagram_team_teitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='teitter',
            new_name='twiter',
        ),
    ]
