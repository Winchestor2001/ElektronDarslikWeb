# Generated by Django 4.1.2 on 2022-10-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_darslik', '0005_resource_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='resource_file/'),
        ),
    ]