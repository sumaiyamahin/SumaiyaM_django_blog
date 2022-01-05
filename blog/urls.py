from django.urls import include, path
from . import views
from rest_framework import routers
from blog.views import PostViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.post_list, name='post_list'),
    path('', views.book_list, name='book_list'),
]