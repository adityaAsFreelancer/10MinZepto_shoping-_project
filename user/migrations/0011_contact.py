# Generated by Django 3.2.4 on 2023-09-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_rename_sprofile_register_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
