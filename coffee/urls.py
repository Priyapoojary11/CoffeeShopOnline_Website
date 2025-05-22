from django.urls import path
from django_distill import distill_path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.login_view, name='root'),  # Redirect root URL to login
    path('', views.home, name='root'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('coffee/<int:coffee_id>/', views.view_coffee, name='view_coffee'),  # URL for viewing specific coffee,
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_checkout/<int:product_id>/', views.add_to_checkout, name='add_to_checkout'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout1/', views.checkout1, name='checkout1'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('profile/', views.profile, name='profile'),
]

# urlpatterns = [
#     path('', views.login_view, name='root'),  # Redirect root URL to login
#     distill_path('signup/', views.signup, name='signup', distill_func=get_signup),
#     distill_path('login/', views.login_view, name='login', distill_func=get_login_view),
#     distill_path('logout/', views.logout_view, name='logout', distill_func=get_logout_view),
#     distill_path('home/', views.home, name='home', distill_func=get_home),
#     distill_path('about/', views.about, name='about', distill_func=about),
#     distill_path('contact/', views.contact, name='contact'),
#     distill_path('gallery/', views.gallery, name='gallery', distill_func=get_gallery),
#     distill_path('coffee/<int:coffee_id>/', views.view_coffee, name='view_coffee', distill_func=get_view_coffee),  # URL for viewing specific coffee,
#     distill_path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart', distill_func=get_add_to_cart),
#     distill_path('add_to_checkout/<int:product_id>/', views.add_to_checkout, name='add_to_checkout', distill_func=get_add_to_checkout),
#     distill_path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart', distill_func=get_remove_from_cart),
#     distill_path('view_cart/', views.view_cart, name='view_cart', distill_func=get_view_cart),
#     distill_path('checkout/', views.checkout, name='checkout', distill_func=get_checkout),
#     distill_path('checkout1/', views.checkout1, name='checkout1', distill_func=get_checkout1),
#     distill_path('payment/<int:order_id>/', views.payment, name='payment', distill_func=get_payment),
#     distill_path('profile/', views.profile, name='profile', distill_func=get_profile),
# ]
# distill_path('', views.index, name='index', distill_func=get_index),