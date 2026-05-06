from __future__ import annotations

import email

from hc.accounts.models import Profile
from hc.api.models import Flip, Notification
from hc.api.transports import Transport, TransportError, get_ping_body
from hc.lib import emails
from hc.lib.signing import sign_bounce_id


class Email(Transport):
    def notify(self, flip: Flip, notification: Notification) -> None:
        return None

    def is_noop(self, status: str) -> bool:
        return False
