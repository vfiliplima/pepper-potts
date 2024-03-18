# Generated by Django 4.2.11 on 2024-03-18 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('queued', 'Queued'), ('in progress', 'In progress'), ('completed', 'Completed')], default='queued', max_length=20),
        ),
    ]
