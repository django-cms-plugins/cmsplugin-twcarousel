from django.contrib import admin
from apps.twcarousel.models import Slide, Carousel


class SlideInline(admin.StackedInline):
    model = Slide


class CarouselAdmin(admin.ModelAdmin):
    model = Carousel

    inlines = [
        SlideInline,
    ]

admin.site.register(Carousel, CarouselAdmin)
