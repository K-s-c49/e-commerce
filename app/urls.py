from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.categorytitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetails.as_view(),name="product-detail"),

    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
