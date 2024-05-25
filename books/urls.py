from django.urls import path
from .views import BookListApiView, book_list_view, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, \
    BookCreateApiView, BookListCreateApiView, BookViewset

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
#     path("books/", BookListApiView.as_view(),),
#     path('books/<int:pk>/', BookDetailApiView.as_view()),
#     path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
#     path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
#     path('books/create/', BookCreateApiView.as_view()),
#     path('booklistcreate/', BookListCreateApiView.as_view()),
#     path('books/', book_list_view),
]

urlpatterns = urlpatterns + router.urls