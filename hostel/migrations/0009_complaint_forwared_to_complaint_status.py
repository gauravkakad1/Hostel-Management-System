# Generated by Django 5.0.1 on 2024-03-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='forwared_to',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]