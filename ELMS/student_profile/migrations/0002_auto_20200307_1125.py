# Generated by Django 2.2 on 2020-03-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile_picture', verbose_name='Profile Picture'),
        ),
    ]
