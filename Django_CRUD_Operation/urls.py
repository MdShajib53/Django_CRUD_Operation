from django.contrib import admin
from django.urls import path, include
from . import SimpleView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('core.urls')),
    path('categories/', include('categories.urls')),
    path('product/', include('product.urls')),
    path('',SimpleView.index),
]
