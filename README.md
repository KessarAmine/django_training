# django_training

Here is my notebook for developing a CRUD API using Django from scratch:
1- Install django rest framework using:
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
2- create a module ("python manage.py app start module_name"), Add ['rest_framework', 'module_name'] to INSTALLED_APPS setting.
3- Create serializers.py and urls.py to moduleFolder.
4- Dev the models, serializers and views.
5- Add endpoints to the urls.py of the modules_folder.
6- Include the urls of the modules_folder to the urls.py of the project Folder.
7- python nabage.py runserver
8- test a get and a post request 
    curl http://127.0.0.1:8000/{endpoint}
    curl -X POST http://127.0.0.1:8000/{endpoint} -H "Content-Type: application/json" -d '{JsonData "key" : "value"}'
9- test Put and delete requests:
    curl -X PUT http://127.0.0.1:8000/api/comments_module/users/1/update/ -H "Content-Type: application/json" -d '{"first_name": "updated_value", "last_name": "updated_value amine", "birthday": "1996-09-25"}'
    curl -X DELETE http://127.0.0.1:8000/api/comments_module/users/1/delete/

Note :
Make sure to put the complexe endpoints before the normal endpoints
have this urls
urlpatterns = [
    path('users/<int:pk>/update/', Users_put.as_view(), name='Users_put'),
    path('users/<int:pk>/delete/', Users_delete.as_view(), name='Users_delete'),
    path('users/<int:pk>/', Users_post_get_id.as_view(), name='user-byid'),
    path('users/', Users_post_get.as_view(), name='users-list'),
]
rather then this
urlpatterns = [
    path('users/', Users_post_get.as_view(), name='users-list'),
    path('users/<int:pk>/update/', Users_put.as_view(), name='Users_put'),
    path('users/<int:pk>/delete/', Users_delete.as_view(), name='Users_delete'),
    path('users/<int:pk>/', Users_post_get_id.as_view(), name='user-byid'),
]
