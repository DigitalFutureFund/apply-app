# Generated by Django 2.2.18 on 2021-02-16 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_customimage_drupal_id'),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('reset_network_people', '0004_add_long_text_to_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetnetworkpeoplepage',
            name='content_bottom_heading',
            field=models.CharField(blank=True, max_length=255, verbose_name='Heading'),
        ),
        migrations.AddField(
            model_name='resetnetworkpeoplepage',
            name='content_bottom_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='resetnetworkpeoplepage',
            name='content_bottom_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page', verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='resetnetworkpeoplepage',
            name='content_bottom_link_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Link text'),
        ),
        migrations.AddField(
            model_name='resetnetworkpeoplepage',
            name='content_bottom_text',
            field=models.TextField(blank=True, verbose_name='Text'),
        ),
    ]
