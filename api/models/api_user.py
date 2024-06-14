from django.db import models


class APIUser(models.Model):
    uuid = models.UUIDField(primary_key=True, blank=False, null=False, auto_created=True)
    username = models.CharField(unique=True, db_index=True, max_length=255)
    password = models.CharField(null=False, max_length=255)
