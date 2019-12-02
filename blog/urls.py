from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/write/', views.make_post, name='make_post'),
    path('post/<pk>/details/', views.post_details, name='post_details'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('post/<pk>/publish/', views.publish_post, name='publish_post'),
    path('post/<pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<pk>/delete/', views.delete_post, name='delete_post'),
    path('post/done/', views.post_done_view, name='post_done'),
    path('post/comment/<pk>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<pk>/move/to/drafts/', views.move_to_draft, name='move_to_drafts'),
    path('post/<pk>/add/like/', views.add_like, name='add_like_to_post'),
    path('post/<pk>/remove/like/', views.remove_like, name='remove_like_from_post'),
    path('post/<pk>/add/like/to/comment/', views.add_like_to_comment, name='add_like_to_comment'),
    path('post/<pk>/remove/like/from/comment/', views.remove_like_from_comment, name='remove_like_from_comment'),
    path('post/<pk>/likes/', views.post_likes, name='post_likes'),
    path('post/<pk>/comment/likes', views.comment_likes, name='comment_likes')
]