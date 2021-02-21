from rest_framework import viewsets, permissions
from rest_framework.status import (
    HTTP_424_FAILED_DEPENDENCY,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_405_METHOD_NOT_ALLOWED,
)
from mailer.mails.models import Mail, Recipient
from mailer.api.serializers import MailSerializer, RecipientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import EmailMessage
from smtplib import SMTPException
from collections import namedtuple
from mailer.mails.models import Recipient
from django.utils import timezone
from .utils import map_recipient_set


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def send(self, request, pk=None):
        mail = self.get_object()

        if mail.sent_at is not None:
            return Response("already sent", status=HTTP_405_METHOD_NOT_ALLOWED)

        recipient_set = Recipient.objects.filter(mail=mail)

        if not recipient_set:
            return Response(
                "no recipients configured", status=HTTP_424_FAILED_DEPENDENCY
            )

        recipients = map_recipient_set(recipient_set)
        print(recipients)

        # try:
        #     EmailMessage(
        #         from_email=(
        #             f'"{mail.from_name}" <{mail.from_address}>'
        #             if mail.from_name
        #             else mail.from_address
        #         ),
        #         subject=mail.subject,
        #         message=mail.body_text,
        #         html_message=mail.body_html,
        #     )
        # except SMTPException as e:
        #     return Response(
        #         f"mail not sent. error: {e}", status=HTTP_500_INTERNAL_SERVER_ERROR
        #     )

        mail.sent_at = timezone.now()
        mail.save()

        return Response({"status": "mail sent", "sent_at": mail.sent_at})


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = [permissions.IsAuthenticated]
