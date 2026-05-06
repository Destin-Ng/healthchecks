from __future__ import annotations

from uuid import UUID

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from hc.accounts.http import AuthenticatedHttpRequest
from hc.api.models import Channel
from hc.integrations.notification import forms

def notification_display(request: AuthenticatedHttpRequest, channel: Channel) -> HttpResponse:
    ctx = {
        "page": "channels",
        "project": channel.project,
        "use_verification": settings.EMAIL_USE_VERIFICATION,
        "form": forms.NotificationForm(),
        "is_new": True,
    }
    return render(request, "notification.html", ctx)
