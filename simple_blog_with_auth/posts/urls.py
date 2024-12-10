from django.urls import path
from .views import AddPostCreateView, EditPostView, DeletePostView

urlpatterns = [
    # path('add/', add_post, name="add_post"),
    path('add/', AddPostCreateView.as_view(), name="add_post"),
    # path('edit/<int:post_id>/',edit_post, name="edit_post"),
    path('edit/<int:post_id>/', EditPostView.as_view(), name="edit_post"),
    # path('delete/<int:post_id>/', delete_post, name="delete_post"),
    path('delete/<int:post_id>/', DeletePostView.as_view(), name="delete_post"),
]
