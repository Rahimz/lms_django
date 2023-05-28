# Generated by Django 4.1.4 on 2023-05-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_course_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('in_review', 'in_review'), ('published', 'published')], default='draft', max_length=25),
        ),
    ]
