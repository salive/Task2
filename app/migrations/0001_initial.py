# Generated by Django 4.0.6 on 2022-07-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Some text')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
            ],
        ),
    ]