# Generated by Django 4.1.4 on 2023-01-03 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_photo_note_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.note'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='photo',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='note_photos', to='app.photo'),
        ),
    ]
