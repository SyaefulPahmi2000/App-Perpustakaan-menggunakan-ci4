from django import views
from django.contrib import admin
from django.urls import path

from . import views
from tugas import views as profilviews
from about import views as aboutviews
from artikelphp import views as artikelphpviews
from artikeldjango import views as artikeldjangoviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', profilviews.index),
    path('about/', aboutviews.index),
    path('artikelphp/', artikelphpviews.index),
    path('artikeldjango/', artikeldjangoviews.index),
    path('', views.index),
]
