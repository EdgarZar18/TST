# Generated by Django 3.1.4 on 2020-12-10 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20201210_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='evidencia_falla',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='ticket_compra',
        ),
    ]
