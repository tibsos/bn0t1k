# Generated by Django 4.1.4 on 2023-01-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_note_archived_note_deleted_note_folders_note_loved_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='folder',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
