# Generated by Django 2.0.1 on 2020-02-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_auto_20200206_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
