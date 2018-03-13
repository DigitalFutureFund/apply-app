# Generated by Django 2.0.2 on 2018-03-01 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_add_intro_to_lab_and_funds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='funds_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labs_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='our_work_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='strapline_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page'),
        ),
    ]
