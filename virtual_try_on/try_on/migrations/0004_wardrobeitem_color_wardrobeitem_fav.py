# Generated by Django 5.1 on 2024-10-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try_on', '0003_remove_userinfo_typesofclothes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wardrobeitem',
            name='color',
            field=models.CharField(default='NA', max_length=50),
        ),
        migrations.AddField(
            model_name='wardrobeitem',
            name='fav',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]