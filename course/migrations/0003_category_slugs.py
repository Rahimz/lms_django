# Generated by Django 4.0.6 on 2022-07-24 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slugs',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]