from __future__ import annotations

from django.urls import path
from hc.integrations.notification import views

urlpatterns = [
    path("index/", views.notification_display, name="hc-notification"),
]
