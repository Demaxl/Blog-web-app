# Generated by Django 4.1.1 on 2023-01-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_blog_cover_image_alter_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.URLField(blank=True, default='https://www.fastcat.com.ph/wp-content/uploads/2016/04/dummy-post-horisontal-thegem-blog-default.jpg'),
        ),
    ]
