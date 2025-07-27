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

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = "__all__"

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"