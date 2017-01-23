from django.db import models
from django.contrib.auth.models import User


class Cours(models.Model):
	name=models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	prof=models.ForeignKey(User)

	class Meta:
		db_table='cours'