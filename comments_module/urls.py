from django.urls import path
from .views import Users_post_get, Users_post_get_id, Users_put, Users_delete

urlpatterns = [
    path('users/<int:pk>/update/', Users_put.as_view(), name='Users_put'),
    path('users/<int:pk>/delete/', Users_delete.as_view(), name='Users_delete'),
    path('users/<int:pk>/', Users_post_get_id.as_view(), name='user-byid'),
    path('users/', Users_post_get.as_view(), name='users-list'),
]
