import uuid

from django.db import models

from children.utils.matviews import MaterializedViewModelMixin
from gifts.utils.readonly import ReadOnlyModel


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


class NaughtyAndNice(ReadOnlyModel, MaterializedViewModelMixin):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    child_name = models.TextField()
    actions = models.TextField()
    wish = models.TextField()     

    class Meta:
        managed = False
        db_table = 'naughties_and_nicies'

    @classmethod
    def _select__sql(cls) -> str:
        return '''
        select 
            row_number() over (ORDER BY c.id) as id,
            c.id as child_id,
            c.name as child_name,
            a.actions as actions,
            l.content as wish
        from operational.children c
        join external.letters l on l.sender_id = c.external_id
        left join (
            select 
                br.child_id as child_id,
                array_agg(br.action) as actions
            from operational.behavior_records br
            group by br.child_id
        ) a on a.child_id = c.id
        '''    