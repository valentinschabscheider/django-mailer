from django.db import models
from uuid import uuid4
from collections import namedtuple
from django.utils.text import Truncator


class Mail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    from_address = models.EmailField()

    from_name = models.CharField(max_length=30, null=True, blank=True)

    subject = models.CharField(max_length=128, null=True, blank=True)

    body_html = models.TextField()

    body_text = models.TextField()

    sent_at = models.DateTimeField(null=True, editable=False)

    @property
    def sent(self):
        return self.sent_at is not None

    def __str__(self):
        return f'{self.from_address}({self.from_name}), "{Truncator(self.body_text).chars(20)}"'

    def __repr__(self):
        return str(
            {
                "id": self.id,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "from": {"address": self.from_address, "name": self.from_name},
                "subject": self.subject,
                "body": {
                    "html": Truncator(self.body_html).chars(20),
                    "text": Truncator(self.body_text).chars(20),
                },
            }
        )

    class Meta:
        ordering = ["created_at", "from_address"]


class Recipient(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)

    TO = "TO"
    CC = "CC"
    BCC = "BCC"

    TYPE_CHOICES = [(TO, "To"), (CC, "Cc"), (BCC, "Bcc")]

    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default=TO)

    address = models.EmailField()

    def __str__(self):
        return f"{self.mail}, {self.type}: {self.address}"

    def __repr__(self):
        return str({"mail": self.mail, "type": self.type, "address": self.address})

    class Meta:
        ordering = ["type", "address"]
        unique_together = ["mail", "type", "address"]
