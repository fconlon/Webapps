# Generated by Django 2.2.3 on 2019-07-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allowance', '0003_auto_20190509_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('users', models.CharField(max_length=100)),
            ],
        ),
    ]