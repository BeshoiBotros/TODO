# Generated by Django 5.0.4 on 2024-04-08 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_app.todo'),
        ),
    ]
