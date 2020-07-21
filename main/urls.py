from django.urls import path
from main import views


urlpatterns = [
	path('register/',views.register, name="register"),

	path('login/', views.login, name="login"),  

    path('logout/',views.logout,name="logout"),

    path('dashboard/',views.dashboard,name="dashboard"),

   path('profile/',views.profile,name="profile"),
    
    path('', views.index, name="index"),
  



]