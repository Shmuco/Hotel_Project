# Generated by Django 3.2.3 on 2021-06-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_rooms_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]