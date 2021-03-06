# Generated by Django 2.2.1 on 2019-05-15 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Teacher'),
        ),
        migrations.AddField(
            model_name='case',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
        migrations.AddField(
            model_name='case',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='cases', to='problem.Tag'),
        ),
    ]
