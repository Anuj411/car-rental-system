# Generated by Django 4.2.5 on 2023-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_baseuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
