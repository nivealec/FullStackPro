from rest_framework import serializers
from api_app.models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id','first_name','last_name','blood']
        
# PatientSerializer: The serializer class is named PatientSerializer, following the convention of naming 
# serializers after their models.
# HyperlinkedModelSerializer: This is a subclass of ModelSerializer, which automatically handles the
# fields and their validation for a given model.
# It also includes a hyperlink for the object (i.e., a URL pointing to the instance's detail view),
# which is often used in APIs to provide a navigable structure.
# For this to work, the related view must have a HyperlinkedIdentityField or use a DefaultRouter.