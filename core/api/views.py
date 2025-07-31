from core import views
from core.models import (
    BannerImage, Chef, MenuCategory, Menu, Event, SocialMedia, 
    Reservation, Testimonial, BlogCategory, Blog, BlogComment,
    GalleryCategory, Gallery, ContactForm, SiteSettings
)
from core.api.serializers import (
    BannerImageSerializer, ChefSerializer, MenuCategorySerializer, MenuSerializer, EventSerializer, ReservationSerializer,
    TestimonialSerializer, BlogCategorySerializer, BlogSerializer, BlogCommentSerializer, BlogRetrieveSerializer, SocialMediaSerializer,
    GalleryRetrieveSerializer, GalleryCategorySerializer, GallerySerializer, ContactFormSerializer, SiteSettingsSerializer
)
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

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

class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class TestimonialListAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class BlogCategoryListAPIView(ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCommentListAPIView(ListAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogRetrieveSerializer

class GalleryCategoryListAPIView(ListAPIView):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer

class GalleryListAPIView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryRetrieveAPIView(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryRetrieveSerializer

class ContactFormCreateAPIView(CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer