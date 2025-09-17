from django.urls import path
from todo.views import custom_sigin,login_page,todo_page,edit_todo,delete_todo,signout,toggle_status
urlpatterns = [
    path('', custom_sigin,name='custom_sigin'),
    path('login/',login_page,name='login'),
    path('todo/',todo_page,name='todopage'),
    path('edit_todo/<int:srno>',view=edit_todo,name='edit_todo'),
    path('delete_todo/<int:srno>',view=delete_todo,name='delete=todo'),
    path("logout/",view=signout,name='signout'),
    path("toggle_status/<int:srno>", toggle_status, name="toggle_status"), 
]

