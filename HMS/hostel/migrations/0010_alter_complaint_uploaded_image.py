# Generated by Django 5.0.1 on 2024-03-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0009_complaint_forwared_to_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='uploaded_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]