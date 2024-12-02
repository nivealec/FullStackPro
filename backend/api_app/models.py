from django.db import models

class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    blood = models.CharField(max_length=50)

    def __str__(self):
     return self.first_name


#The class Patient inherits from models.Model, which is the base class for all Django models.
# This makes Patient a model that Django will use to interact with the database.

# The __str__ method is a special Python method that defines how an instance of the class should be 
# represented as a string.




