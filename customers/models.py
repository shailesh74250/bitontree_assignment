from django.db import models

class Customer(models.Model):
	first_name = models.CharField("First name", max_length=255)
	last_name = models.CharField("Last name", max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	# appointment_date_time = models.DateField("Appointment At", auto_now_add=True, blank=True, null=True)
	createdAt = models.DateTimeField("Created At", auto_now_add=True,)
	# modifiedAt = models.DateTimeField('Modified At', auto_now=True)
	
	def __str__(self):
		return self.first_name