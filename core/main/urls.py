from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('flights/', views.FlightsListView.as_view(), name='flights'),
    path('aboutus/', views.AboutListView.as_view(), name='about'),
    path('stays/', views.StaysListView.as_view(), name='stays'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('register/', views.register_request, name='register'),
    path('LOGIN/', views.login_request, name='login'),
    path('logout', views.logout_request, name = 'logout'),


]