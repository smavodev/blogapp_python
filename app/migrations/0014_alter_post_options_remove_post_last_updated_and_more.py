# Generated by Django 4.2.3 on 2023-07-31 21:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_alter_websitemeta_options_profile_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title', 'modified_date'], 'verbose_name': 'posts', 'verbose_name_plural': 'posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='app.tag'),
        ),
    ]
