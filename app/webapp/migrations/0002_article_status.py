# Generated by Django 4.1.1 on 2022-09-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Активна'), ('NOT_ACTIVE', 'Не Активна')], default='ACTIVE', max_length=100, verbose_name='Статус'),
        ),
    ]