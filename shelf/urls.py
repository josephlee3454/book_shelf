from django.urls import path
from . import views	
urlpatterns = [
    path('', views.make_book),
    path('authors/',views.make_author),
    path('view_book/<int:book_id>', views.view_book),
    path('view_author/<int:author_id>', views.view_author),
]