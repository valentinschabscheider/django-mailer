from rest_framework import serializers
from mailer.mails.models import Mail, Recipient

from .utils import map_recipient_set


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ["mail", "type", "address"]
        # extra_kwargs = {"mail": {"write_only": True}}


class MailSerializer(serializers.ModelSerializer):

    # recipients = RecipientSerializer(many=True, read_only=True, source="recipient_set")

    recipients = serializers.SerializerMethodField("get_mail_recipients")

    def get_mail_recipients(self, instance):
        return map_recipient_set(instance.recipient_set.all())._asdict()

    class Meta:
        model = Mail
        fields = [
            "id",
            "created_at",
            "updated_at",
            "from_address",
            "from_name",
            "subject",
            "body_html",
            "body_text",
            "recipients",
            "sent_at",
        ]
