from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    # path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signin/profilepage/', views.profilepage, name='profilepage'),
    path('profilepage/upload/', views.upload, name='upload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
