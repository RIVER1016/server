# Generated by Django 2.2.1 on 2019-05-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=20)),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'demo',
            },
        ),
    ]