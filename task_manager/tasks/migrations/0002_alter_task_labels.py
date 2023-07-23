# Generated by Django 4.2.3 on 2023-07-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Labels',
            field=models.ManyToManyField(related_name='Tasks', through='tasks.TaskLabel', to='status.Labels', verbose_name='Labels'),
        ),
    ]
