# Generated by Django 3.2.4 on 2023-09-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cpic', models.ImageField(null=True, upload_to='static/category')),
                ('cdate', models.DateField(max_length=30, null=True)),
            ],
        ),
    ]
