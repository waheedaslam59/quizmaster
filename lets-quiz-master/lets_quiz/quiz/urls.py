from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import play
app_name = 'quiz'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user-home$', views.user_home, name='user_home'),
    path('play/', views.play, name='play'),
    path('play/<int:id>/', views.play, name='play'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register, name='register'),

]
