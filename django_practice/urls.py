from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls'), {'age': 20}, 'poll'),
    path('admin/', admin.site.urls),
]