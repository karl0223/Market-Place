from django.urls import path

from . import views

app_name = "conversation"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("<int:pk>/", views.detail, name="detail"),
    path("new/<int:item_pk>/", views.new_conversation, name="new"),
    path("concern/", views.concern_messages, name="concern"),
    path("<str:email>/action", views.concern_action, name="action"),
    path("<int:pk>/delete", views.delete_concern_message, name="delete"),
    path("submit-action/<str:email>/", views.submit_action, name="submit_action"),
]
