# Generated by Django 4.0.3 on 2022-06-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(max_length=8, null=True),
        ),
    ]