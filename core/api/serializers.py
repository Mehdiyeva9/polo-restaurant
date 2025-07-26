from rest_framework import serializers
from core.models import (
    BannerImage, Chef, MenuCategory, Menu, Event, 
    Reservation, Testimonial, BlogCategory, Blog, Blogcomment,
    GalleryCategory, Gallery, ContactForm, SiteSettings
)

class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = "__all__"

