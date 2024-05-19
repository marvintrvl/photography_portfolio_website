from django.urls import path
from .views import base_view, IndexView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photos'
urlpatterns = [
    path('base/', base_view, name='base'),
    path('', IndexView.as_view(), name='index'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)