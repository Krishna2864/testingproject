from Self_Drive.models import *
from rest_framework import serializers

# Create your models here.


class Admin_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Admin_Management
            fields=('__all__')


class User_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=User_Management
            fields=('__all__')


class Vehicle_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Vehicle_Management
            fields=('__all__')


class List_your_vehicles_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=List_your_vehicles_Management
            fields=('__all__')


class Vehicle_MonitoringSerailizer(serializers.Serializer):
    class  meta:
            model=Vehicle_Monitoring
            fields=('__all__')


class Co_partnner_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Co_partnner_Management
            fields=('__all__')


class Country_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Country_Management
            fields=('__all__')


class state_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=state_Management
            fields=('__all__')


class City_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=City_Management
            fields=('__all__')


class Advertisement_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Advertisement_Management
            fields=('__all__')


class Listing_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Listing_Management
            fields=('__all__')


class Templates_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Templates_Management
            fields=('__all__')


class Fare_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Fare_Management
            fields=('__all__')


class Notification_To_UserSerailizer(serializers.Serializer):
    class  meta:
            model=Notification_To_User
            fields=('__all__')


class Notification_To_CoPartnerSerailizer(serializers.Serializer):
    class  meta:
            model=Notification_To_CoPartner
            fields=('__all__')


class Fuel_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Fuel_Management
            fields=('__all__')


class Maintainance_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Maintainance_Management
            fields=('__all__')


class Refral_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Refral_Management
            fields=('__all__')


class Refund_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Refund_Management
            fields=('__all__')


class Transaction_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Transaction_Management
            fields=('__all__')


class FeedbackSerailizer(serializers.Serializer):
    class  meta:
            model=Feedback
            fields=('__all__')


class Content_ManagementSerailizer(serializers.Serializer):
    class  meta:
            model=Content_Management
            fields=('__all__')


class SOSSerailizer(serializers.Serializer):
    class  meta:
            model=SOS
            fields=('__all__')


class SupportSerailizer(serializers.Serializer):
    class  meta:
            model=Support
            fields=('__all__')


class Terms_ConditionSerailizer(serializers.Serializer):
    class  meta:
            model=Terms_Condition
            fields=('__all__')


class Privacy_PolicySerailizer(serializers.Serializer):
    class  meta:
            model=Privacy_Policy
            fields=('__all__')


