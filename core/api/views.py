from core import views
from core.models import (
    BannerImage, Chef, MenuCategory, Menu, Event, 
    Reservation, Testimonial, BlogCategory, Blog, BlogComment,
    GalleryCategory, Gallery, ContactForm, SiteSettings
)
from core.api.serializers import (
    BannerImageSerializer, ChefSerializer, MenuCategorySerializer, MenuSerializer, EventSerializer,
    ReservationSerializer, TestimonialSerializer, BlogCategorySerializer, BlogSerializer, BlogCommentSerializer,
    GalleryCategorySerializer, GallerySerializer, ContactFormSerializer, SiteSettingsSerializer
)
from rest_framework.generics import ListAPIView

class BannerImageListAPIView(ListAPIView):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer

class ChefListAPIView(ListAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ReservationListAPIView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = EventSerializer