from Taxi_Service.models import *
from rest_framework import serializers

# Create your models here.

class DashBoardSerailizer(serializers.Serializer):
    class Meta:
        model=DashBoard
        fields=('__all__')


class Admin_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Admin_Management
        fields=('__all__')


class User_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=User_Management
        fields=('__all__')

class Vehicle_ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle_Management
        fields=('__all__')

class Co_partnner_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Co_partnner_Management
        fields=('__all__')


class Country_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Country_Management
        fields=('__all__')

class Advertisement_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement_Management
        fields=('__all__')

class State_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=State_Management
        fields=('__all__')


class City_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=City_Management
        fields=('__all__')

class Listing_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Listing_Management
        fields=('__all__')

class City1Serailizer(serializers.Serializer):
    class Meta:
        model=City1
        fields=('__all__')
class RENTALSerailizer(serializers.Serializer):
    class Meta:
        model=RENTAL
        fields=('__all__')


class OUTSTATATION_SecondSerailizer(serializers.Serializer):
    class Meta:
        model=OUTSTATATION_Second
        fields=('__all__')


class Templates_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Templates_Management
        fields=('__all__')


class Fare_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Fare_Management
        fields=('__all__')


class CitySerailizer(serializers.Serializer):
    class Meta:
        model=City
        fields=('__all__')


class OUTSTATATIONSerailizer(serializers.Serializer):
    class Meta:
        model=OUTSTATATION
        fields=('__all__')


class Notification_To_DriverSerailizer(serializers.Serializer):
    class Meta:
        model=Notification_To_Driver
        fields=('__all__')


class Notification_To_CustomerSerailizer(serializers.Serializer):
    class Meta:
        model=Notification_To_Customer
        fields=('__all__')


class Fuel_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Fuel_Management
        fields=('__all__')


class Maintainance_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Maintainance_Management
        fields=('__all__')


class Refral_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Refral_Management
        fields=('__all__')
    



class Transaction_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Transaction_Management
        fields=('__all__')


class Drive_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=Drive_Management
        fields=('__all__')


class SOSSerailizer(serializers.Serializer):
    class Meta:
        model=SOS
        fields=('__all__')


class SupportSerailizer(serializers.Serializer):
    class Meta:
        model=Support
        fields=('__all__')


class List_your_vehicles_ManagementSerailizer(serializers.Serializer):
    class Meta:
        model=List_your_vehicles_Management
        fields=('__all__')

class Terms_ConditionSerailizer(serializers.Serializer):
    class Meta:
        model=Terms_Condition
        fields=('__all__')


class Privacy_PolicySerailizer(serializers.Serializer):
    class Meta:
        model=Privacy_Policy
        fields=('__all__')
