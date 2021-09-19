from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'quiz'
urlpatterns = [
    path('', views.home, name='home'),
    # path('addQuestion/', addQuestion,name='addQuestion'),
    path('startquiz/<int:id>', views.startquiz, name='startquiz'),
    path('startquiz/', views.startquiz, name='startquiz'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)