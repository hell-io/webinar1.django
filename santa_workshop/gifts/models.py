import uuid
from django.db import models

from gifts.utils.readonly import ReadOnlyModel


class Letter(ReadOnlyModel):
    id = models.UUIDField(primary_key=True)
    sender_id = models.UUIDField()
    country = models.TextField()
    address = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'letters'


# class Gift(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)