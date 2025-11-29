"""
URL configuration for website_amnhac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from music import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("albums/", views.albums_store, name="albums"),
    path("events/", views.events, name="events"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("dangky/",views.register_view, name="dangky"),
        path("xacthuc/<int:user_id>/", views.activate_account, name="activate"),
    path("customer/", views.customer, name="customer"),
    path("logout",views.logout_views, name="logout"),
    path('album/<int:album_id>/', views.albums_detail, name='albums_detail'),
    # path("cart/", views.view_cart, name="view_cart"),
]

# Phục vụ static files trong development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
