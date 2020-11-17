from django.db import models


class GeneralModel(models.Model):
    access_to_management = models.BooleanField(default=False)
