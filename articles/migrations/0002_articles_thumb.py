# Generated by Django 4.0.4 on 2022-05-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]