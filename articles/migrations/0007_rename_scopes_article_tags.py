# Generated by Django 4.1.5 on 2023-01-15 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_options_rename_scopes_scope_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tags',
        ),
    ]
