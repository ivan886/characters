from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from characters import views_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path("characters/", include('characters.urls', namespace="characters")),
    path("universes/", include('characters.urls_universes', namespace="universes")),
    path("users/login", views_users.login_v, name="login"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
