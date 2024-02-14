
from django.urls import path,include
from todo import views
urlpatterns = [
    path('',views.todo_list,name="todo_list"),
    path('deletedata/<int:id>/',views.delete_data,name="deletedata"),
    path('search',views.search,name="search")
]
