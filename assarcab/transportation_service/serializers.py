from transportation_service.models import *
from rest_framework import serializers

# Create your models here.


class Vehicle_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Vehicle_Management
        fields=('__all__')


class Driver_MangementSerailizer(serializers.Serializer):
    class Meta:
        model=Driver_Mangement
        fields=('__all__')



class Copartner_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Copartner_Management
        fields=('__all__')



class Country_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Country_Management
        fields=('__all__')



class State_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=State_Management
        fields=('__all__')



class City_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=City_Management
        fields=('__all__')



class Advertisement_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Advertisement_Management
        fields=('__all__')



class Refral_mangemntSerailizer(serializers.Serializer):
    class Meta:
        model=Refral_mangemnt
        fields=('__all__')



class Notification_to_DriverSerailizer(serializers.Serializer):
    class Meta:
        model=Notification_to_Driver
        fields=('__all__')



class Fuel_MangementSerailizer(serializers.Serializer):
    class Meta:
        model=Fuel_Mangement
        fields=('__all__')



class Maintenance_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Maintenance_Management
        fields=('__all__')



class fARE_MGMTSerailizer(serializers.Serializer):
    class Meta:
        model=fARE_MGMT
        fields=('__all__')



class Listing_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Listing_Management
        fields=('__all__')



class OUTSTATIONSerailizer(serializers.Serializer):
    class Meta:
        model=OUTSTATION
        fields=('__all__')



class Transaction_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Transaction_Management
        fields=('__all__')



class LIST_YOUR_VEHICLE_MGMTSerailizer(serializers.Serializer):
    class Meta:
        model=LIST_YOUR_VEHICLE_MGMT
        fields=('__all__')



class FeedbackSerailizer(serializers.Serializer):
    class Meta:
        model=Feedback
        fields=('__all__')



class TERMS_CONDITIONSSerailizer(serializers.Serializer):
    class Meta:
        model=TERMS_CONDITIONS
        fields=('__all__')



class PRIVACY_POLICYSerailizer(serializers.Serializer):
    class Meta:
        model=PRIVACY_POLICY
        fields=('__all__')

