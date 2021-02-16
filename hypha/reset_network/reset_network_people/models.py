from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from hypha.reset_network.reset_network_person.models import ResetNetworkPerson
from hypha.reset_network.reset_network_utils.models import ResetNetworkBasePage


class ResetNetworkPeoplePage(ResetNetworkBasePage):
    class Meta:
        verbose_name = "Reset Network People Page"

    parent_page_types = ['reset_network_home.ResetNetworkHomePage']
    subpage_types = []

    content_heading = models.CharField(verbose_name='Heading', max_length=255, blank=False)
    content_text = models.TextField(verbose_name='Text', blank=True)
    content_long_text = RichTextField(verbose_name='Text', blank=True)

    section_1 = StreamField(
        [
            ('sub_heading', blocks.CharBlock(icon='tag')),
            ('sub_text', blocks.TextBlock()),
            ('persons', blocks.ListBlock(
                blocks.StructBlock([
                    ('person', SnippetChooserBlock(ResetNetworkPerson)),
                ], icon='user'), icon='group'
            )),
        ],
        verbose_name='Content - Section 1 (People)',
        blank=True
    )

    content_bottom_heading = models.CharField(verbose_name='Heading', max_length=255, blank=True)
    content_bottom_text = models.TextField(verbose_name='Text', blank=True)
    content_bottom_image = models.ForeignKey('images.CustomImage', verbose_name='Image', null=True, blank=True,
                                             related_name='+', on_delete=models.SET_NULL)
    content_bottom_link = models.ForeignKey('wagtailcore.Page', verbose_name='Link', null=True, blank=True, related_name='+',
                                            on_delete=models.PROTECT)
    content_bottom_link_text = models.CharField(verbose_name='Link text', max_length=255, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('content_heading'),
            FieldPanel('content_text'),
            FieldPanel('content_long_text'),
        ], heading='Content'),
        StreamFieldPanel('section_1'),
        MultiFieldPanel([
            FieldPanel('content_bottom_heading'),
            FieldPanel('content_bottom_text'),
            ImageChooserPanel('content_bottom_image'),
            PageChooserPanel('content_bottom_link'),
            FieldPanel('content_bottom_link_text')
        ], heading='Content bottom'),
    ]
