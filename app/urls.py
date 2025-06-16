from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,mypasswordchangeform,MySetPasswordForm
from .views import customLogoutView
urlpatterns = [
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.categorytitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetails.as_view(),name="product-detail"),
    path("profile/", views.profileview.as_view(),name="profile"),
    path("address/", views.address,name="address"),
    path("updateaddress/<int:pk>", views.updateaddress.as_view(),name="updateaddress"),

    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="showcart"),
    path("checkout/", views.checkout.as_view(), name="checkout"),
    path("paymentdone/",views.payment_done, name="paymentdone"),
    path("orders/",views.orders, name="orders"),
    
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
    path("pluswishlist/", views.plus_wishlist,),
    path("minuswishlist/", views.minus_wishlist),
    
    path("search/", views.search, name="search"),
    path("wishlist/", views.show_wishlist, name="showwishlist"),

    
    #login authentication
    path("registration/", views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path("account/login", auth_view.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm) , name="login"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="app/password_rest.html", form_class=MyPasswordResetForm) , name="password_rest"),
    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name="app/changepassword.html",form_class=mypasswordchangeform, success_url='/passwordchangedone') , name="passwordchange"),
    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),
    path('logout/', customLogoutView.as_view() , name='logout'),

    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="app/password_rest.html",form_class=MyPasswordResetForm), name="password_rest"), 
    path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name="app/password_rest_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=MySetPasswordForm),name="password_reset_confirm"),
    path("password-reset-complete/",auth_view.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"), name="password_reset_complete"),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "K-SHOP"
admin.site.site_title = "K-SHOP"
admin.site.site_index_title = "WELCOME TO K-SHOP"
