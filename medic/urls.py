from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),   # 👈 HOME PAGE
    path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),
    path("appointment/", views.appointment, name="appointment"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("team/", views.team, name="team"),
    path("service/", views.service, name="service"),
    path("search/", views.search, name="search"),
    path("price/", views.price, name="price"),
    path("details/", views.details, name="details"),
    path("about/", views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) if hasattr(settings, 'STATIC_ROOT') else []
