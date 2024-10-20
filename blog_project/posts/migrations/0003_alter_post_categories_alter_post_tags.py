# Generated by Django 5.1.1 on 2024-10-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_tag_post_created_at_post_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='posts', to='posts.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='posts.tag'),
        ),
    ]
