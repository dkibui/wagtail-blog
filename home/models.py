from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)   

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class ContactPage(Page):
    heading = models.CharField(max_length=255, blank=False, null=False)
    body = RichTextField(blank=True)   

    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("body"),
    ]