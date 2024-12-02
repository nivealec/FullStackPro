from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Patient
from api_app.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



# This code defines a Django REST Framework (DRF) ViewSet called PatientViewSet for handling operations 
# on the Patient model.

# viewsets.ModelViewSet:
# A built-in DRF class that provides default implementations for common actions like list, create, retrieve, 
# update, and destroy.

# queryset: Specifies the data the viewset will operate on.
# Patient.objects.all(): Fetches all objects from the Patient model in the database.
# This queryset will be used for operations like listing and retrieving objects.

# serializer_class: Specifies the serializer to be used for converting data between Python objects and JSON.
# PatientSerializer: A serializer (defined elsewhere) that maps the Patient model to a JSON representation 
# and handles validation.

