from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from hypha.reset_network.reset_network_utils.models import ResetNetworkBasePage


class ResetNetworkWorkPagePillar(Orderable):

    page = ParentalKey('reset_network_work.ResetNetworkWorkPage', related_name='reset_network_work_pillar',
                       on_delete=models.CASCADE)

    heading = models.CharField(verbose_name='Heading', max_length=255, blank=False)
    text = models.TextField(verbose_name='Text', blank=True)
    image = models.ForeignKey('images.CustomImage', null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    panels = [
        FieldPanel('heading'),
        FieldPanel('text'),
        ImageChooserPanel('image'),
    ]


class ResetNetworkWorkPageRegion(Orderable):

    page = ParentalKey('reset_network_work.ResetNetworkWorkPage', related_name='reset_network_work_region',
                       on_delete=models.CASCADE)

    heading = models.CharField(verbose_name='Heading', max_length=255, blank=False)
    text = RichTextField(verbose_name='Text', blank=True)

    panels = [
        FieldPanel('heading'),
        FieldPanel('text'),
    ]


class ResetNetworkWorkPage(ResetNetworkBasePage):

    class Meta:
        verbose_name = "Reset Network Work Page"

    parent_page_types = ['reset_network_home.ResetNetworkHomePage']
    subpage_types = []

    content_heading = models.CharField(verbose_name='Heading', max_length=255, blank=False)
    content_text = models.TextField(verbose_name='Text', blank=True)
    content_long_text = RichTextField(verbose_name='Text', blank=True)

    region_heading = models.CharField(verbose_name='Heading', max_length=255, null=True, blank=True)

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
        MultiFieldPanel([
            InlinePanel('reset_network_work_pillar', label='Pillar', heading='Pillar')
        ], heading='content - Pillars'),
        MultiFieldPanel([
            FieldPanel('region_heading'),
            InlinePanel('reset_network_work_region', label='Region', heading='Region')
        ], heading='Content - Regions'),
        MultiFieldPanel([
            FieldPanel('content_bottom_heading'),
            FieldPanel('content_bottom_text'),
            ImageChooserPanel('content_bottom_image'),
            PageChooserPanel('content_bottom_link'),
            FieldPanel('content_bottom_link_text')
        ], heading='Content bottom'),
    ]
