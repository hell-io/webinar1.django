import uuid
from django.db import models


class Child(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.UUIDField()
    name = models.TextField()

    class Meta:
        db_table = 'children'
        managed = True


class BehaviorRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    action = models.TextField()
    
    class Meta:
        db_table = 'operational\".\"behavior_records'
        managed = True