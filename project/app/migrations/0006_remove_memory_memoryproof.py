# Generated by Django 5.2.1 on 2025-05-29 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_memory_memoryproof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memory',
            name='memoryproof',
        ),
    ]
