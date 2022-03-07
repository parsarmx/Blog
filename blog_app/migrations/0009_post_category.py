# Generated by Django 3.2 on 2022-02-02 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog_app.subcategory'),
            preserve_default=False,
        ),
    ]