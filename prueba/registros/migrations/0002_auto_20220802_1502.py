# Generated by Django 3.0.14 on 2022-08-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='matricula',
            field=models.CharField(max_length=12, verbose_name='Mat'),
        ),
    ]
