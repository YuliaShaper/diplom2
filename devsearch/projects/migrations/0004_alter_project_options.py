# Generated by Django 5.0.6 on 2024-07-13 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_options_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_ratio', 'title']},
        ),
    ]
