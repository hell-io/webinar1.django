from django.db import models


class Elf(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    class Meta:
        db_table = 'elves'


class Craftsman(Elf):
    craft = models.CharField(max_length=200)

    class Meta:
        db_table = 'craftsmen'


class Courier(Elf):
    country = models.CharField(max_length=150)

    class Meta:
        db_table = 'couriers'