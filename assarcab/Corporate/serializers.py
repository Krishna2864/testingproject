from .models import *
from rest_framework import serializers

# Create your models here.


class Admin_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Admin_Management
        fields=('__all__')


class User_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=User_Management
        fields=('__all__')



class Vehicle_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle_Management
        fields=('__all__')



class Driver_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Driver_Mangement
        fields=('__all__')



class Co_partner_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Co_partner_Management
        fields=('__all__')



class Country_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Country_Management
        fields=('__all__')



class State_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=State_Management
        fields=('__all__')



class City_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=City_Management
        fields=('__all__')



class Advertisement_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement_Management
        fields=('__all__')



class Refral_MangemntSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Refral_Mangemnt
        fields=('__all__')



class Notification_to_DriverSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Driver
        fields=('__all__')



class Notification_to_RidderSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Ridder
        fields=('__all__')



class Fuel_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fuel_Mangement
        fields=('__all__')



class Maintenance_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Maintenance_Management
        fields=('__all__')



class  Listing_ASSIGN_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Listing_ASSIGN_Management
        fields=('__all__')



class OUTSTATION_SecondSerailizer(serializers.ModelSerializer):
    class Meta:
        model=OUTSTATION_Second
        fields=('__all__')



class LOCALSerailizer(serializers.ModelSerializer):
    class Meta:
        model=LOCAL
        fields=('__all__')



class EMPLOYEE_TRANSPORTATION_FourthSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TRANSPORTATION_Fourth
        fields=('__all__')



class EMPLOYEE_TAXISerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TAXI
        fields=('__all__')



class Templates_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Templates_Management
        fields=('__all__')



class Fare_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fare_Management
        fields=('__all__')



class OUTSTATIONSerailizer(serializers.ModelSerializer):
    class Meta:
        model=OUTSTATION
        fields=('__all__')



class LOCAL_SecondSerailizer(serializers.ModelSerializer):
    class Meta:
        model=LOCAL_Second
        fields=('__all__')



class EMPLOYEE_TRANSPORTATION_FifthSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TRANSPORTATION_Fifth
        fields=('__all__')



class EMPLOYEE_TAXI_SecondSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TAXI_Second
        fields=('__all__')



class Route_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Route_Management
        fields=('__all__')



class EMPLOYEE_TRANSPORTATION_SixthSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TRANSPORTATION_Sixth
        fields=('__all__')



class Pickup_Point_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Pickup_Point_Management
        fields=('__all__')


class  dropup_Points_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model= dropup_Points_Management
        fields=('__all__')

class EMPLOYEE_TRANSPORTATION_ThirdSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TRANSPORTATION_Third
        fields=('__all__')



class EMPLOYEE_TRANSPORTATION_SecondSerailizer(serializers.ModelSerializer):
    class Meta:
        model=EMPLOYEE_TRANSPORTATION_Second
        fields=('__all__')



class Transaction_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Transaction_Management
        fields=('__all__')



class LIST_YOUR_VEHICLE_MGMTSerailizer(serializers.ModelSerializer):
    class Meta:
        model=LIST_YOUR_VEHICLE_MGMT
        fields=('__all__')



class FeedbackSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=('__all__')



class SOSSerailizer(serializers.ModelSerializer):
    class Meta:
        model=SOS
        fields=('__all__')



class Support_HELPSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Support_HELP
        fields=('__all__')



class TERMS_CONDITIONSSerailizer(serializers.ModelSerializer):
    class Meta:
        model=TERMS_CONDITIONS
        fields=('__all__')



class PRIVACY_POLICYSerailizer(serializers.ModelSerializer):
    class Meta:
        model=PRIVACY_POLICY
        fields=('__all__')

