# Generated by Django 4.2.3 on 2023-08-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='gender',
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(choices=[('Sdy', 'Study'), ('Slp', 'Sleep'), ('Fd', 'Food'), ('Nmz', 'Namaz'), ('Prb', 'Problem Solving'), ('aply', 'Job Apply'), ('Rsn', 'Topic Revision'), ('Explore', 'Explore New Technology'), ('Eng', 'Practice English')], max_length=10),
        ),
    ]
