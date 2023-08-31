from django.urls import path
from Tasks.views import home, add_todo,Login,Logout,Signup,delete_todo, change_todo
urlpatterns = [
    path('', home,name='home'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', Signup, name='signup'),
    path('add_todo/', add_todo, name='add_todo'),
    path('delete_todo/<int:id>/', delete_todo, name='delete_todo'),
    path('change_todo/<int:id>/<str:status>/', change_todo, name='change_todo'),
]
