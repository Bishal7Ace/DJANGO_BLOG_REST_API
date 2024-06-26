# Generated by Django 5.0.3 on 2024-04-11 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=55)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='anime_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='anime_name',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='blog_app.category'),
        ),
    ]
