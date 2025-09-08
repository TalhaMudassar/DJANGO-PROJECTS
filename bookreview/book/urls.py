from django.urls import path
from book import views
urlpatterns = [
    path('',views.book_list, name='book_list'),
    path('book/new', views.book_create, name='book-create'),
    path('book/<int:pk>',views.book_detail,name='book_detail'),
    path('book/<int:pk>/edit',views.book_update,name='book_update'),
    path('book/<int:pk>/delete',views.book_delete,name='book_delete'),
    
]


