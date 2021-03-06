# Generated by Django 2.2.5 on 2021-05-23 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210523_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_image', models.ImageField(upload_to='post_content_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
        ),
    ]
