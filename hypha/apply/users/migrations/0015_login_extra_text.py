# Generated by Django 2.2.19 on 2021-03-16 08:45

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_usersettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='extra_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='consent_help',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='consent_show',
            field=models.BooleanField(default=False, verbose_name='Show consent checkbox'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='consent_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
