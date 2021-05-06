# Generated by Django 3.0.5 on 2021-05-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbcrypto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='temp', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
