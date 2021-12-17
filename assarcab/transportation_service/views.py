from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

#3
from .models import Vehicle_Management
from .serializers import Vehicle_ManagementSerailizer
@api_view(['GET'])
def vehicleList(request):
    vehicle=Vehicle_Management.objects.all()
    if vehicle is None:
        JsonResponse("No records")
    else:
      serializer=Vehicle_ManagementSerailizer(vehicle,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def vehicleDetail(request,pk):
    vehicle=Vehicle_Management.objects.get(id=pk)
    serializer=Vehicle_ManagementSerailizer(vehicle,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def vehicleCreate(request):
    serializer=Vehicle_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def vehicleUpdate(request,pk):
    vehicle=Vehicle_Management.objects.get(id=pk)
    serializer=Vehicle_ManagementSerailizer(instance=vehicle,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def vehicleDelete(request,pk):
    vehicle=Vehicle_Management.objects.get(id=pk)
    vehicle.delete()
    return JsonResponse("Deleted")

#4

from .models import Driver_Mangement
from .serializers import Driver_MangementSerailizer
@api_view(['GET'])
def driverList(request):
    driver=Driver_Mangement.objects.all()
    if Driver_Mangement is None:
        JsonResponse("No records")
    else:
      serializer=Driver_MangementSerailizer(driver,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def driverDetail(request,pk):
    driver=Driver_Mangement.objects.get(id=pk)
    serializer=Driver_MangementSerailizer(driver,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def driverCreate(request):
    serializer=Driver_MangementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def driverUpdate(request,pk):
    driver=Driver_Mangement.objects.get(id=pk)
    serializer=Driver_MangementSerailizer(instance=driver,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def driverDelete(request,pk):
    driver=Driver_Mangement.objects.get(id=pk)
    driver.delete()
    return JsonResponse("Deleted")

#5

from .models import Country_Management
from .serializers import Country_ManagementSerailizer
@api_view(['GET'])
def countryList(request):
    country=Country_Management.objects.all()
    if country is None:
        JsonResponse("No records")
    else:
      serializer=Country_ManagementSerailizer(country,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def countryDetail(request,pk):
    country=Country_Management.objects.get(id=pk)
    serializer=Country_ManagementSerailizer(country,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def countryCreate(request):
    serializer=Country_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def countryUpdate(request,pk):
    country=Country_Management.objects.get(id=pk)
    serializer=Country_ManagementSerailizer(instance=country,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def countryDelete(request,pk):
    country=Country_Management.objects.get(id=pk)
    country.delete()
    return JsonResponse("Deleted")

#6

from .models import State_Management
from .serializers import State_ManagementSerailizer
@api_view(['GET'])
def stateList(request):
    state=State_Management.objects.all()
    if state is None:
        JsonResponse("No records")
    else:
      serializer=State_ManagementSerailizer(state,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def stateDetail(request,pk):
    state=State_Management.objects.get(id=pk)
    serializer=State_ManagementSerailizer(state,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def stateCreate(request):
    serializer=State_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def stateUpdate(request,pk):
    state=State_Management.objects.get(id=pk)
    serializer=State_ManagementSerailizer(instance=state,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def stateDelete(request,pk):
    state=State_Management.objects.get(id=pk)
    state.delete()
    return JsonResponse("Deleted")
#7
from .models import City_Management
from .serializers import City_ManagementSerailizer
@api_view(['GET'])
def cityList(request):
    city=City_Management.objects.all()
    if city is None:
        JsonResponse("No records")
    else:
      serializer=City_ManagementSerailizer(city,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def cityDetail(request,pk):
    city=City_Management.objects.get(id=pk)
    serializer=City_ManagementSerailizer(city,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def cityCreate(request):
    serializer=City_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def cityUpdate(request,pk):
    city=City_Management.objects.get(id=pk)
    serializer=City_ManagementSerailizer(instance=city,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def cityDelete(request,pk):
    city=City_Management.objects.get(id=pk)
    city.delete()
    return JsonResponse("Deleted")

#8
from .models import Advertisement_Management
from .serializers import Advertisement_ManagementSerailizer
@api_view(['GET'])
def advertismentList(request):
    advertisment=Advertisement_Management.objects.all()
    if advertisment is None:
        JsonResponse("No records")
    else:
      serializer=Advertisement_ManagementSerailizer(advertisment,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def advertismentDetail(request,pk):
    advertisment=Advertisement_Management.objects.get(id=pk)
    serializer=Advertisement_ManagementSerailizer(advertisment,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def advertismentCreate(request):
    serializer=Advertisement_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def advertismentUpdate(request,pk):
    advertisment=Advertisement_Management.objects.get(id=pk)
    serializer=Advertisement_ManagementSerailizer(instance=advertisment,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def advertismentDelete(request,pk):
    advertisment=Advertisement_Management.objects.get(id=pk)
    advertisment.delete()
    return JsonResponse("Deleted")

#9
from .models import Refral_mangemnt
from .serializers import Refral_mangemntSerailizer
@api_view(['GET'])
def refralList(request):
    refral=Refral_mangemnt.objects.all()
    if refral is None:
        JsonResponse("No records")
    else:
      serializer=Refral_mangemntSerailizer(refral,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def refralDetail(request,pk):
    refral=Refral_mangemnt.objects.get(id=pk)
    serializer=Refral_mangemntSerailizer(refral,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refralCreate(request):
    serializer=Refral_mangemntSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refralUpdate(request,pk):
    refral=Refral_mangemnt.objects.get(id=pk)
    serializer=Refral_mangemntSerailizer(instance=refral,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def refralDelete(request,pk):
    refral=Refral_mangemnt.objects.get(id=pk)
    refral.delete()
    return JsonResponse("Deleted")


#11
from .models import Fuel_Mangement
from .serializers import Fuel_MangementSerailizer

@api_view(['GET'])
def fuelList(request):
    fuel=Fuel_Mangement.objects.all()
    if fuel is None:
        JsonResponse("No records")
    else:
      serializer=Fuel_MangementSerailizer(fuel,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def fuelDetail(request,pk):
    fuel=Fuel_Mangement.objects.get(id=pk)
    serializer=Fuel_MangementSerailizer(fuel,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fuelCreate(request):
    serializer=Fuel_MangementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fuelUpdate(request,pk):
    fuel=Fuel_Mangement.objects.get(id=pk)
    serializer=Fuel_MangementSerailizer(instance=fuel,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def fuelDelete(request,pk):
    fuel=Fuel_Mangement.objects.get(id=pk)
    fuel.delete()
    return JsonResponse("Deleted")

#12
from .models import Maintenance_Management
from .serializers import Maintenance_ManagementSerailizer
@api_view(['GET'])
def maintenanceList(request):
    maintenance=Maintenance_Management.objects.all()
    if maintenance is None:
        JsonResponse("No records")
    else:
      serializer=Maintenance_ManagementSerailizer(maintenance,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def maintenanceDetail(request,pk):
    maintenance=Maintenance_Management.objects.get(id=pk)
    serializer=Maintenance_ManagementSerailizer(maintenance,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def maintenanceCreate(request):
    serializer=Maintenance_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def maintenanceUpdate(request,pk):
    maintenance=Maintenance_Management.objects.get(id=pk)
    serializer=Maintenance_ManagementSerailizer(instance=maintenance,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def maintenanceDelete(request,pk):
    maintenance=Maintenance_Management.objects.get(id=pk)
    maintenance.delete()
    return JsonResponse("Deleted")
#14
from .models import fARE_MGMT
from .serializers import fARE_MGMTSerailizer
@api_view(['GET'])
def fareList(request):
    fare=fARE_MGMT.objects.all()
    if fare is None:
        JsonResponse("No records")
    else:
      serializer=fARE_MGMTSerailizer(fare,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def fareDetail(request,pk):
    fare=fARE_MGMT.objects.get(id=pk)
    serializer=fARE_MGMTSerailizer(fare,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fareCreate(request):
    serializer=fARE_MGMTSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fareUpdate(request,pk):
    fare=fARE_MGMT.objects.get(id=pk)
    serializer=fARE_MGMTSerailizer(instance=fare,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def fareDelete(request,pk):
    fare=fARE_MGMT.objects.get(id=pk)
    fare.delete()
    return JsonResponse("Deleted")

#19

from .models import Copartner_Management
from .serializers import Copartner_ManagementSerailizer
@api_view(['GET'])
def co_partnerList(request):
    co_partner=Copartner_Management.objects.all()
    if co_partner is None:
        JsonResponse("No records")
    else:
      serializer=Copartner_ManagementSerailizer(co_partner,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def co_partnerDetail(request,pk):
    co_partner=Copartner_Management.objects.get(id=pk)
    serializer=Copartner_ManagementSerailizer(co_partner,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def co_partnerCreate(request):
    serializer=Copartner_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def co_partnerUpdate(request,pk):
    co_partner=Copartner_Management.objects.get(id=pk)
    serializer=Copartner_ManagementSerailizer(instance=co_partner,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def co_partnerDelete(request,pk):
    co_partner=Copartner_Management.objects.get(id=pk)
    co_partner.delete()
    return JsonResponse("Deleted")
#21
from .models import Notification_to_Driver
from .serializers import Notification_to_DriverSerailizer
@api_view(['GET'])
def notification_to_driverList(request):
    notification_to_driver=Notification_to_Driver.objects.all()
    if notification_to_driver is None:
        JsonResponse("No records")
    else:
      serializer=Notification_to_DriverSerailizer(notification_to_driver,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def notification_to_driverDetail(request,pk):
    notification_to_driver=Notification_to_Driver.objects.get(id=pk)
    serializer=Notification_to_DriverSerailizer(notification_to_driver,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_driverCreate(request):
    serializer=Notification_to_DriverSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_driverUpdate(request,pk):
    notification_to_driver=Notification_to_Driver.objects.get(id=pk)
    serializer=Notification_to_DriverSerailizer(instance=notification_to_driver,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def notification_to_driverDelete(request,pk):
    notification_to_driver=Notification_to_Driver.objects.get(id=pk)
    notification_to_driver.delete()
    return JsonResponse("Deleted")
#23
from .models import Transaction_Management
from .serializers import Transaction_ManagementSerailizer
@api_view(['GET'])
def transactionList(request):
    transaction=Transaction_Management.objects.all()
    if transaction is None:
        JsonResponse("No records")
    else:
      serializer=Transaction_ManagementSerailizer(transaction,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def transactionDetail(request,pk):
    transaction=Transaction_Management.objects.get(id=pk)
    serializer=Transaction_ManagementSerailizer(transaction,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def transactionCreate(request):
    serializer=Transaction_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def transactionUpdate(request,pk):
    transaction=Transaction_Management.objects.get(id=pk)
    serializer=Transaction_ManagementSerailizer(instance=transaction,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def transactionDelete(request,pk):
    transaction=Transaction_Management.objects.get(id=pk)
    transaction.delete()
    return JsonResponse("Deleted")

#24
from .models import LIST_YOUR_VEHICLE_MGMT
from .serializers import LIST_YOUR_VEHICLE_MGMTSerailizer
@api_view(['GET'])
def list_your_vehicleList(request):
    list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.all()
    if list_your_vehicle is None:
        JsonResponse("No records")
    else:
      serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(list_your_vehicle,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def list_your_vehicleDetail(request,pk):
    list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
    serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(list_your_vehicle,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def list_your_vehicleCreate(request):
    serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def list_your_vehicleUpdate(request,pk):
    list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
    serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(instance=list_your_vehicle,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def list_your_vehicleDelete(request,pk):
    list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
    list_your_vehicle.delete()
    return JsonResponse("Deleted")

#25
from .models import Feedback
from .serializers import FeedbackSerailizer
@api_view(['GET'])
def feedbackList(request):
    feedback=Feedback.objects.all()
    if feedback is None:
        JsonResponse("No records")
    else:
      serializer=FeedbackSerailizer(feedback,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def feedbackDetail(request,pk):
    feedback=Feedback.objects.get(id=pk)
    serializer=FeedbackSerailizer(feedback,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def feedbackCreate(request):
    serializer=FeedbackSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def feedbackUpdate(request,pk):
    feedback=Feedback.objects.get(id=pk)
    serializer=FeedbackSerailizer(instance=feedback,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def feedbackDelete(request,pk):
    feedback=Feedback.objects.get(id=pk)
    feedback.delete()
    return JsonResponse("Deleted")

#29
from .models import TERMS_CONDITIONS
from .serializers import TERMS_CONDITIONSSerailizer
@api_view(['GET'])
def term_conditionList(request):
    term_condition=TERMS_CONDITIONS.objects.all()
    if term_condition is None:
        JsonResponse("No records")
    else:
      serializer=TERMS_CONDITIONS(term_condition,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def term_conditionDetail(request,pk):
    term_condition=TERMS_CONDITIONS.objects.get(id=pk)
    serializer=TERMS_CONDITIONSSerailizer(term_condition,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def term_conditionCreate(request):
    serializer=TERMS_CONDITIONSSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def term_conditionUpdate(request,pk):
    term_condition=TERMS_CONDITIONS.objects.get(id=pk)
    serializer=TERMS_CONDITIONSSerailizer(instance=term_condition,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def term_conditionDelete(request,pk):
    term_condition=TERMS_CONDITIONS.objects.get(id=pk)
    term_condition.delete()
    return JsonResponse("Deleted")

#30
from .models import PRIVACY_POLICY
from .serializers import PRIVACY_POLICYSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def privacy_policyList(request):
    privacy_policy=PRIVACY_POLICY.objects.all()
    if privacy_policy is None:
        JsonResponse("No records")
    else:
      serializer=PRIVACY_POLICYSerailizer(privacy_policy,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def privacy_policyDetail(request,pk):
    privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
    serializer=PRIVACY_POLICYSerailizer(privacy_policy,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def privacy_policyCreate(request):
    serializer=PRIVACY_POLICYSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def privacy_policyUpdate(request,pk):
    privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
    serializer=PRIVACY_POLICYSerailizer(instance=privacy_policy,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def privacy_policyDelete(request,pk):
    privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
    privacy_policy.delete()
    return JsonResponse("Deleted")
#22
from .models import OUTSTATION
from .serializers import OUTSTATIONSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def outstationList(request):
    privacy_policy=OUTSTATION.objects.all()
    if privacy_policy is None:
        JsonResponse("No records")
    else:
      serializer=OUTSTATIONSerailizer(privacy_policy,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def outstationDetail(request,pk):
    privacy_policy=OUTSTATION.objects.get(id=pk)
    serializer=OUTSTATIONSerailizer(privacy_policy,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def outstationCreate(request):
    serializer=OUTSTATIONSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def outstationUpdate(request,pk):
    privacy_policy=OUTSTATION.objects.get(id=pk)
    serializer=OUTSTATIONSerailizer(instance=privacy_policy,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def outstationDelete(request,pk):
    privacy_policy=OUTSTATION.objects.get(id=pk)
    privacy_policy.delete()
    return JsonResponse("Deleted")


#22
from .models import Listing_Management
from .serializers import Listing_ManagementSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def listingList(request):
    privacy_policy=Listing_Management.objects.all()
    if privacy_policy is None:
        JsonResponse("No records")
    else:
      serializer=Listing_ManagementSerailizer(privacy_policy,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def listingDetail(request,pk):
    privacy_policy=Listing_Management.objects.get(id=pk)
    serializer=Listing_ManagementSerailizer(privacy_policy,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def listingCreate(request):
    serializer=Listing_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def listingUpdate(request,pk):
    privacy_policy=Listing_Management.objects.get(id=pk)
    serializer=Listing_ManagementSerailizer(instance=privacy_policy,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def listingDelete(request,pk):
    privacy_policy=Listing_Management.objects.get(id=pk)
    privacy_policy.delete()
    return JsonResponse("Deleted")


