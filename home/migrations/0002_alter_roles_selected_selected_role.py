# Generated by Django 5.0.2 on 2024-03-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles_selected',
            name='selected_role',
            field=models.CharField(max_length=200),
        ),
    ]