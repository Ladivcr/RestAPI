# Generated by Django 3.2.8 on 2021-10-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='ID',
            field=models.CharField(max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
