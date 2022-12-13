from django.contrib.auth.views import PasswordChangeView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from .views import RegisterView

app_name = 'myapp'

urlpatterns = [
    path('', views.main_page_view, name='home'),
    path('categories/<str:string>/', views.main_page_view, name='categories'),
    path('admin/', admin.site.urls, name='admin'),
    path('registration/', RegisterView.as_view(), name='registration'),
    # path('kitchen/', views.kitchen_view, name='kitchen'),
    # path('bedroom/', views.bedroom_view, name='bedroom'),
    # path('lamps/', views.lamps_view, name='lamps'),
    path('customise/', views.creative_products_view, name='customise'),
    path('about/', views.about_info_view, name='about'),
    path('request/', views.creative_order_view, name='request'),
    path('information/', views.user_info_view, name='userInfo'),
    path('change_password/', PasswordChangeView.as_view(template_name='registration/passwordChange.html'), name='passwordChange'),
    path('password_change/done/', PasswordChangeView.as_view(), name='password_change_done'),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
