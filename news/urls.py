from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('add_to_bookmark/<int:id>', views.add_to_bookmark, name="add_to_bookmark"),
    path('bookmarks/', views.bookmark_list, name="bookmark_list"),

    path('', views.latest, name="latest"),
    path('archive/', views.archive, name="archive")
]
