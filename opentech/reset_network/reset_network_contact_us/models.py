from django.db import models
from opentech.reset_network.reset_network_utils.models import ResetNetworkBasePage
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class ResetNetworkContactUsPage(ResetNetworkBasePage):
    class Meta:
        verbose_name = "Reset Network Contact Us Page"

    parent_page_types = ['reset_network_home.ResetNetworkHomePage']
    subpage_types = []

    content_heading = models.CharField(verbose_name='Heading', max_length=255, blank=False)
    content_text = RichTextField(verbose_name='Text', blank=True)
    content_email = models.EmailField(verbose_name='Email', null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('content_heading'),
            FieldPanel('content_text'),
            FieldPanel('content_email'),
        ], heading='Content'),
    ]
