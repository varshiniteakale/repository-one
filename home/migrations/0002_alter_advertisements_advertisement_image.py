# Generated by Django 3.2.8 on 2021-10-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='advertisement_image',
            field=models.ImageField(upload_to='C:\\Users\\bitra\\varshini-project\\varshini_project\\media'),
        ),
    ]