# Generated by Django 4.2 on 2024-07-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2000)),
                ('Synopsis', models.TextField(max_length=300)),
            ],
        ),
    ]
