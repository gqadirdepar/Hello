# Generated by Django 3.1.5 on 2021-01-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('Phone', models.CharField(max_length=122)),
                ('Desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]