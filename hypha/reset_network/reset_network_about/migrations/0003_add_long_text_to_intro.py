# Generated by Django 2.2.18 on 2021-02-15 09:46

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reset_network_about', '0002_auto_20200303_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetnetworkaboutpage',
            name='content_long_text',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Text'),
        ),
    ]
