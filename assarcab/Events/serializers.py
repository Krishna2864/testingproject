from .models import *
from rest_framework import serializers



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


class Refund_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Refund_Management
        fields=('__all__')


class Fuel_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fuel_Mangement
        fields=('__all__')


class Maintenance_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Maintenance_Management
        fields=('__all__')


class Route_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Route_Management
        fields=('__all__')


class Fare_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fare_Management
        fields=('__all__')

class Fare_ManagementOutStationSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fare_Management_Outstation
        fields=('__all__')

class Fare_ManagementLocalSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fare_Management_Local
        fields=('__all__')





class TIME_SCHEDULE_MGMTSerailizer(serializers.ModelSerializer):
    class Meta:
        model=TIME_SCHEDULE_MGMT
        fields=('__all__')


class Pickup_Point_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Pickup_Point_Management
        fields=('__all__')


class DROPUp_Point_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=DROPUp_Point_Management
        fields=('__all__')


class Listing_ASSIGN_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Listing_ASSIGN_Management
        fields=('__all__')


class Co_partner_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Co_partner_Management
        fields=('__all__')


class Notification_to_RidderSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Ridder
        fields=('__all__')


class Notification_to_DriverSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Driver
        fields=('__all__')


class Consignment_TrackingSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Consignment_Tracking
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


class Seat_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Seat_Mangement
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





