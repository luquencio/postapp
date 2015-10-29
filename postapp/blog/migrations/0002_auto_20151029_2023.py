# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='descr',
        ),
        migrations.AddField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='media/postsimages', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='media/postsimages', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='media/postsimages', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='media/postsimages', null=True),
        ),
    ]
