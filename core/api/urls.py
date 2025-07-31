from django.conf import urls
from django.urls import path
from core.api import views

urlpatterns = [
    path("bannerimage-list/", views.BannerImageListAPIView.as_view()),
    path("chef-list/", views.ChefListAPIView.as_view()),
    path("menucategory-list/", views.MenuCategoryListAPIView.as_view()),
    path("menu-list/", views.MenuListAPIView.as_view()),
    path("event-list/", views.EventListAPIView.as_view()),
    path("reservation-create/", views.ReservationCreateAPIView.as_view()),
    path("testimonial-list/", views.TestimonialListAPIView.as_view()),
    path("blogcategory-list/", views.BlogCategoryListAPIView.as_view()),
    path("blog-list/", views.BlogListAPIView.as_view())
]