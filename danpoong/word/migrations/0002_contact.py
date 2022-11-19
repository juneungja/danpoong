# Generated by Django 4.1.3 on 2022-11-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
