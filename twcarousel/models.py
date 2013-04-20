from django.db import models
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField


class Carousel(CMSPlugin):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Slide(models.Model):

    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to="slides")
    title = models.CharField(max_length=250)
    text = HTMLField(blank=True)
    carousel = models.ForeignKey(Carousel)
