# Generated by Django 4.1.2 on 2022-11-01 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_director_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='director_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.director'),
        ),
    ]
