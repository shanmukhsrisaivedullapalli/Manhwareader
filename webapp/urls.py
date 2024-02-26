from django.urls import path
from .views import home, getmanga, getmangachapter,loginUser,logoutUser

urlpatterns = [
    path("", home, name='home'),
    path("manga/<int:manga_id>/", getmanga, name='getmanga'),
    path("manga/<int:manga_id>/chapter/<int:chapter_number>/", getmangachapter, name='getmangachapter'),
    path("login/", loginUser, name='loginUser'),
    path("logout/", logoutUser, name='logoutUser'),
]
