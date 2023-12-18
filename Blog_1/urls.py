from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app1.views import login, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path("accounts/login/", login , name='login'),
    path("logout/", CustomLogoutView.as_view() , name='logout'),
    path('blog/', include('blogs.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)