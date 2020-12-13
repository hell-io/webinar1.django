from django.db import models


class ReadOnlyException(Exception):
    def __init__(self, attribute):
        message = "'{}' method is not allowed for a read-only model"
        super().__init__(message.format(attribute.__name__))


class ReadOnlyManager(models.Manager):
    def create(self, *args, **kwargs):
        raise ReadOnlyException(self.create)

    def get_or_create(self, *args, **kwargs):
        raise ReadOnlyException(self.get_or_create)

    def update_or_create(self, *args, **kwargs):
        raise ReadOnlyException(self.update_or_create)

    def update(self, *args, **kwargs):
        raise ReadOnlyException(self.update)

    def bulk_create(self, *args, **kwargs):
        raise ReadOnlyException(self.bulk_create)

    def bulk_update(self, *args, **kwargs):
        raise ReadOnlyException(self.bulk_update)     
    
    def delete(self, *args, **kwargs):
        raise ReadOnlyException(self.delete)
       

class ReadOnlyModel(models.Model):
    objects = ReadOnlyManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        raise ReadOnlyException(self.save)

    def delete(self, *args, **kwargs):
        raise ReadOnlyException(self.delete)   


class ReadOnlyAdminMixin(object):
    """Disables all editing capabilities."""
    actions = None

    # We cannot call super().get_fields(request, obj) because that method calls
    # get_readonly_fields(request, obj), causing infinite recursion. Ditto for
    # super().get_form(request, obj). So we  assume the default ModelForm.
    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request, *args, **kwargs):
        return False

    # Allow viewing objects but not actually changing them.
    def has_change_permission(self, request, obj=None):
        return (request.method in ['GET', 'HEAD'] and
                super().has_change_permission(request, obj))

    def has_delete_permission(self, request, obj=None):
        return False