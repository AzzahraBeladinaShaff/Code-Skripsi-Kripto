# Generated by Django 5.0.4 on 2024-05-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='encrypted_file',
            field=models.FileField(blank=True, null=True, upload_to='files/encrypted'),
        ),
        migrations.AlterField(
            model_name='file',
            name='key',
            field=models.CharField(max_length=256),
        ),
    ]