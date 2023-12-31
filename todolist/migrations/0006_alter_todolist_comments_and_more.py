# Generated by Django 4.2.7 on 2023-12-06 03:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_todolist_email_todolist_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='comments',
            field=models.TextField(blank=True, default='default_comments', null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='datetime_field',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='email',
            field=models.EmailField(blank=True, default='default_email', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(default='default_name', max_length=50),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='username',
            field=models.CharField(default='default_username', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='value',
            field=models.PositiveSmallIntegerField(default='default_value', null=True),
        ),
    ]
