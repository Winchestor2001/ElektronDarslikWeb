# Generated by Django 4.1.2 on 2022-10-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_darslik', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='resource_img/'),
        ),
    ]
