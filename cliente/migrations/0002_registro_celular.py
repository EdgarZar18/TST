# Generated by Django 3.1.4 on 2020-12-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='celular',
            field=models.CharField(default='', max_length=10, verbose_name='celular'),
            preserve_default=False,
        ),
    ]
