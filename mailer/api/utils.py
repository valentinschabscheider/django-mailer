from django.db.models.query import QuerySet


def map_recipient_set(recipient_set: QuerySet):
    recipients = {"to": (), "cc": (), "bcc": ()}

    for type in recipients.keys():
        recipients[type] = tuple(
            recipient_set.filter(type=type).values_list("address", flat=True)
        )

    return recipients