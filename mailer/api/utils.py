from django.db.models.query import QuerySet
from collections import namedtuple

from mailer.mails.models import Recipient


def map_recipient_set(recipient_set: QuerySet):
    def create_tuple(type):
        return recipient_set.filter(type=type).values_list("address", flat=True)

    return namedtuple("ApiRecipientType", ["to", "cc", "bcc"])(
        to=create_tuple(Recipient.TO),
        cc=create_tuple(Recipient.CC),
        bcc=create_tuple(Recipient.BCC),
    )