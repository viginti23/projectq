from django.urls import path
from home import views as home_views
from startparty import views as startparty_views


urlpatterns = [
    path('', startparty_views.startparty, name='startparty'),
]
