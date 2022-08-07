# Generated by Django 4.0.6 on 2022-07-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blog/image')),
            ],
        ),
    ]