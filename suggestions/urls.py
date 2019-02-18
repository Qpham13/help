from django.urls import path

from . import views
app_name='suggestions'


urlpatterns = [
    path('', views.get_suggest, name='get_suggest'),
    path('<int:sugg_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('list/', views.list, name='list'),
    path('<int:sugg_id>/vote/',views.vote,name='vote'),
    # ex: /polls/5/vote/
]