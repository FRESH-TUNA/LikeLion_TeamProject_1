from django.urls import include, path
from . import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('<int:post_id>/detail', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('<int:post_id>/update', views.update, name="update"),
    path('<int:post_id>/delete', views.delete, name="delete"),
    path('<int:post_id>/addComment', views.addComment, name="addComment"),
]