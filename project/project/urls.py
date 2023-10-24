from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login',views.LoginPage,name='login'),
    path('home',views.HomePage,name='home'),
    path('logout',views.LogoutPage,name='logout'),

    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('projects',views.projects,name='projects'),
    path('resume',views.resume,name='resume'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)