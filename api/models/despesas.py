from django.db import models


class Despesa(models.Model):
    value = models.FloatField(null=False)
    name = models.CharField(max_length=255, null=False)

    transaction_date = models.DateField(auto_now_add=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    user_uuid = models.ForeignKey("APIUser", on_delete=models.CASCADE)
