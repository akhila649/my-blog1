# Generated by Django 2.2.5 on 2019-09-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('locality', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('pincode', models.TextField()),
            ],
        ),
    ]