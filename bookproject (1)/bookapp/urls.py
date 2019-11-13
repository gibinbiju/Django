from django.urls import path
from bookapp import views

urlpatterns=[
    path('',views.book_list,name='book_list'),
    path('view/<int:pk>',views.book_view,name='book_view'),
    path('edit/<int:pk>',views.book_edit,name='book_edit'),
    path('create/',views.book_create,name='book_create'),
]