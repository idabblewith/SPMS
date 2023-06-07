from django.urls import path
from . import views

urlpatterns = [
    path("comments", views.Comments.as_view()),
    path("comments/<int:pk>", views.CommentDetail.as_view()),
    path("direct_messages", views.DirectMessages.as_view()),
    path("direct_messages/<int:pk>", views.DirectMessageDetail.as_view()),
    path("chat_rooms", views.ChatRooms.as_view()),
    path("chat_rooms/<int:pk>", views.ChatRoomDetail.as_view()),
    path("comment_reactions", views.CommentReactions.as_view()),
    path("comment_reactions/<int:pk>", views.CommentReactionDetail.as_view()),
    path("direct_message_reactions", views.DirectMessageReactions.as_view()),
    path(
        "direct_message_reactions/<int:pk>", views.DirectMessageReactionDetail.as_view()
    ),
]
