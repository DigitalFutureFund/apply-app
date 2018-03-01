# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-13 15:10
from __future__ import unicode_literals

from django.db import migrations
import opentech.apply.categories.blocks
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0021_rename_workflow_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationsubmission',
            name='form_fields',
            field=wagtail.core.fields.StreamField((('text_markup', wagtail.core.blocks.RichTextBlock(group='Other', label='Paragraph')), ('char', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('text', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('number', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('checkbox', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('default_value', wagtail.core.blocks.BooleanBlock(required=False))), group='Fields')), ('radios', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))), group='Fields')), ('dropdown', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))), group='Fields')), ('checkboxes', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('checkboxes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Checkbox')))), group='Fields')), ('date', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateBlock(required=False))), group='Fields')), ('time', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TimeBlock(required=False))), group='Fields')), ('datetime', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateTimeBlock(required=False))), group='Fields')), ('image', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('file', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('rich_text', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('category', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(help_text='Leave blank to use the default Category label', label='Label', required=False)), ('help_text', wagtail.core.blocks.TextBlock(label='Leave blank to use the default Category help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('category', opentech.apply.categories.blocks.ModelChooserBlock('categories.Category')), ('multi', wagtail.core.blocks.BooleanBlock(label='Multi select', required=False))), group='Custom')), ('title', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('value', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('email', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('address', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required')), ('full_name', wagtail.core.blocks.StructBlock((('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.core.blocks.static_block.StaticBlock())), group='Required'))), default=[]),
            preserve_default=False,
        ),
    ]
