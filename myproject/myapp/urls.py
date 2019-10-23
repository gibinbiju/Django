from django.urls import path
from django.views.generic import TemplateView

from myapp import views

urlpatterns = [
    path("index",views.index,name="index1"),
    path("indexview", views.IndexView.as_view(), name="index1"),
    path("indexviewwithmessage", views.IndexView.as_view(message="Hello With Message"), name="index1"),
    path("messageview", views.MessageView.as_view(), name="messageview")
]

