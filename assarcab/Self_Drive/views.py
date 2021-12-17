from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Admin_Management
from .serializers import Admin_ManagementSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
#1
@api_view(['GET'])
def adminList(request):
    admin1=Admin_Management.objects.all()
    if admin1 is None:
        JsonResponse("No records")
    else:
      serializer=Admin_ManagementSerailizer(admin1,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def adminDetail(request,pk):
    admin1=Admin_Management.objects.get(id=pk)
    serializer=Admin_ManagementSerailizer(admin1,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def adminCreate(request):
    serializer=Admin_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def adminUpdate(request,pk):
    admin1=Admin_Management.objects.get(id=pk)
    serializer=Admin_ManagementSerailizer(instance=admin1,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def adminDelete(request,pk):
    admin1=Admin_Management.objects.get(id=pk)
    admin1.delete()
    return JsonResponse("Deleted")
#2
from .models import User_Management
from .serializers import User_ManagementSerailizer
@api_view(['GET'])
def userList(request):
    user=User_Management.objects.all()
    if user is None:
        JsonResponse("No records")
    else:
      serializer=User_ManagementSerailizer(user,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def userDetail(request,pk):
    user=User_Management.objects.get(id=pk)
    serializer=User_ManagementSerailizer(user,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def userCreate(request):
    serializer=User_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def userUpdate(request,pk):
    user=User_Management.objects.get(id=pk)
    serializer=User_ManagementSerailizer(instance=user,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def userDelete(request,pk):
    user=User_Management.objects.get(id=pk)
    user.delete()
    return JsonResponse("Deleted")

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

#5

from .models import state_Management
from .serializers import state_ManagementSerailizer
@api_view(['GET'])
def stateList(request):
    state=state_Management.objects.all()
    if state is None:
        JsonResponse("No records")
    else:
      serializer=state_ManagementSerailizer(state,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def stateDetail(request,pk):
    state=state_Management.objects.get(id=pk)
    serializer=state_ManagementSerailizer(state,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def stateCreate(request):
    serializer=state_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def stateUpdate(request,pk):
    state=state_Management.objects.get(id=pk)
    serializer=state_ManagementSerailizer(instance=state,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def stateDelete(request,pk):
    state=state_Management.objects.get(id=pk)
    state.delete()
    return JsonResponse("Deleted")
#6
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

#7
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

#8
from .models import Refral_Management
from .serializers import Refral_ManagementSerailizer
@api_view(['GET'])
def refralList(request):
    refral=Refral_Management.objects.all()
    if refral is None:
        JsonResponse("No records")
    else:
      serializer=Refral_ManagementSerailizer(refral,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def refralDetail(request,pk):
    refral=Refral_Management.objects.get(id=pk)
    serializer=Refral_ManagementSerailizer(refral,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refralCreate(request):
    serializer=Refral_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refralUpdate(request,pk):
    refral=Refral_Management.objects.get(id=pk)
    serializer=Refral_ManagementSerailizer(instance=refral,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def refralDelete(request,pk):
    refral=Refral_Management.objects.get(id=pk)
    refral.delete()
    return JsonResponse("Deleted")

#9
from .models import Refund_Management
from .serializers import Refund_ManagementSerailizer
@api_view(['GET'])
def refundList(request):
    refund=Refund_Management.objects.all()
    if refund is None:
        JsonResponse("No records")
    else:
      serializer=Refund_ManagementSerailizer(refund,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def refundDetail(request,pk):
    refund=Refund_Management.objects.get(id=pk)
    serializer=Refund_ManagementSerailizer(refund,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refundCreate(request):
    serializer=Refund_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def refundUpdate(request,pk):
    refund=Refund_Management.objects.get(id=pk)
    serializer=Refund_ManagementSerailizer(instance=refund,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def refundDelete(request,pk):
    refund=Refund_Management.objects.get(id=pk)
    refund.delete()
    return JsonResponse("Deleted")

#10
from .models import Fuel_Management
from .serializers import Fuel_ManagementSerailizer

@api_view(['GET'])
def fuelList(request):
    fuel=Fuel_Management.objects.all()
    if fuel is None:
        JsonResponse("No records")
    else:
      serializer=Fuel_ManagementSerailizer(fuel,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def fuelDetail(request,pk):
    fuel=Fuel_Management.objects.get(id=pk)
    serializer=Fuel_ManagementSerailizer(fuel,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fuelCreate(request):
    serializer=Fuel_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fuelUpdate(request,pk):
    fuel=Fuel_Management.objects.get(id=pk)
    serializer=Fuel_ManagementSerailizer(instance=fuel,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def fuelDelete(request,pk):
    fuel=Fuel_Management.objects.get(id=pk)
    fuel.delete()
    return JsonResponse("Deleted")

#11
from .models import Maintainance_Management
from .serializers import Maintainance_ManagementSerailizer
@api_view(['GET'])
def maintenanceList(request):
    maintenance=Maintainance_Management.objects.all()
    if maintenance is None:
        JsonResponse("No records")
    else:
      serializer=Maintainance_ManagementSerailizer(maintenance,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def maintenanceDetail(request,pk):
    maintenance=Maintainance_Management.objects.get(id=pk)
    serializer=Maintainance_ManagementSerailizer(maintenance,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def maintenanceCreate(request):
    serializer=Maintainance_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def maintenanceUpdate(request,pk):
    maintenance=Maintainance_Management.objects.get(id=pk)
    serializer=Maintainance_ManagementSerailizer(instance=maintenance,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def maintenanceDelete(request,pk):
    maintenance=Maintainance_Management.objects.get(id=pk)
    maintenance.delete()
    return JsonResponse("Deleted")

#12
from .models import Fare_Management
from .serializers import Fare_ManagementSerailizer
@api_view(['GET'])
def fareList(request):
    fare=Fare_Management.objects.all()
    if fare is None:
        JsonResponse("No records")
    else:
      serializer=Fare_ManagementSerailizer(fare,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def fareDetail(request,pk):
    fare=Fare_Management.objects.get(id=pk)
    serializer=Fare_ManagementSerailizer(fare,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fareCreate(request):
    serializer=Fare_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def fareUpdate(request,pk):
    fare=Fare_Management.objects.get(id=pk)
    serializer=Fare_ManagementSerailizer(instance=fare,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def fareDelete(request,pk):
    fare=Fare_Management.objects.get(id=pk)
    fare.delete()
    return JsonResponse("Deleted")
#13
from .models import Co_partnner_Management
from .serializers import Co_partnner_ManagementSerailizer
@api_view(['GET'])
def co_partnerList(request):
    co_partner=Co_partnner_Management.objects.all()
    if co_partner is None:
        JsonResponse("No records")
    else:
      serializer=Co_partnner_ManagementSerailizer(co_partner,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def co_partnerDetail(request,pk):
    co_partner=Co_partnner_Management.objects.get(id=pk)
    serializer=Co_partnner_ManagementSerailizer(co_partner,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def co_partnerCreate(request):
    serializer=Co_partnner_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def co_partnerUpdate(request,pk):
    co_partner=Co_partnner_Management.objects.get(id=pk)
    serializer=Co_partnner_ManagementSerailizer(instance=co_partner,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def co_partnerDelete(request,pk):
    co_partner=Co_partnner_Management.objects.get(id=pk)
    co_partner.delete()
    return JsonResponse("Deleted")

#14
from .models import Notification_To_CoPartner
from .serializers import Notification_To_CoPartnerSerailizer
@api_view(['GET'])
def notification_to_copartnerList(request):
    notification_to_copartner=Notification_To_CoPartner.objects.all()
    if notification_to_copartner is None:
        JsonResponse("No records")
    else:
      serializer=Notification_To_CoPartnerSerailizer(notification_to_copartner,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def notification_to_copartnerDetail(request,pk):
    notification_to_copartner=Notification_To_CoPartner.objects.get(id=pk)
    serializer=Notification_To_CoPartnerSerailizer(notification_to_copartner,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_copartnerCreate(request):
    serializer=Notification_To_CoPartnerSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_copartnerUpdate(request,pk):
    notification_to_copartner=Notification_To_CoPartner.objects.get(id=pk)
    serializer=Notification_To_CoPartnerSerailizer(instance=notification_to_copartner,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def notification_to_copartnerDelete(request,pk):
    notification_to_copartner=Notification_To_CoPartner.objects.get(id=pk)
    notification_to_copartner.delete()
    return JsonResponse("Deleted")

#15
from .models import Notification_To_User
from .serializers import Notification_To_UserSerailizer
@api_view(['GET'])
def notification_to_userList(request):
    notification_to_user=Notification_To_User.objects.all()
    if notification_to_user is None:
        JsonResponse("No records")
    else:
      serializer=Notification_To_UserSerailizer(notification_to_user,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def notification_to_userDetail(request,pk):
    notification_to_user=Notification_To_User.objects.get(id=pk)
    serializer=Notification_To_UserSerailizer(notification_to_user,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_userCreate(request):
    serializer=Notification_To_UserSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def notification_to_userUpdate(request,pk):
    notification_to_user=Notification_To_User.objects.get(id=pk)
    serializer=Notification_To_UserSerailizer(instance=notification_to_user,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def notification_to_userDelete(request,pk):
    notification_to_user=Notification_To_User.objects.get(id=pk)
    notification_to_user.delete()
    return JsonResponse("Deleted")

#16
from .models import Content_Management
from .serializers import Content_ManagementSerailizer
@api_view(['GET'])
def contentList(request):
    content_tracking=Content_Management.objects.all()
    if content_tracking is None:
        JsonResponse("No records")
    else:
      serializer=Content_ManagementSerailizer(content_tracking,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def contentDetail(request,pk):
    content_tracking=Content_Management.objects.get(id=pk)
    serializer=Content_ManagementSerailizer(content_tracking,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def contentCreate(request):
    serializer=Content_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def contentUpdate(request,pk):
    content_tracking=Content_Management.objects.get(id=pk)
    serializer=Content_ManagementSerailizer(instance=content_tracking,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def contentDelete(request,pk):
    content_tracking=Content_Management.objects.get(id=pk)
    content_tracking.delete()
    return JsonResponse("Deleted")

#17
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
#18
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

#19
from .models import SOS
from .serializers import SOSSerailizer
@api_view(['GET'])
def sosList(request):
    sos=SOS.objects.all()
    if sos is None:
        JsonResponse("No records")
    else:
      serializer=SOSSerailizer(sos,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def sosDetail(request,pk):
    sos=SOS.objects.get(id=pk)
    serializer=SOSSerailizer(sos,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def sosCreate(request):
    serializer=SOSSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def sosUpdate(request,pk):
    sos=SOS.objects.get(id=pk)
    serializer=SOSSerailizer(instance=sos,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def sosDelete(request,pk):
    sos=SOS.objects.get(id=pk)
    sos.delete()
    return JsonResponse("Deleted")
#20
from .models import Support
from .serializers import SupportSerailizer
@api_view(['GET'])
def support_helpList(request):
    support_help=Support.objects.all()
    if support_help is None:
        JsonResponse("No records")
    else:
      serializer=SupportSerailizer(support_help,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def support_helpDetail(request,pk):
    support_help=Support.objects.get(id=pk)
    serializer=SupportSerailizer(support_help,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def support_helpCreate(request):
    serializer=SupportSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def support_helpUpdate(request,pk):
    support_help=Support.objects.get(id=pk)
    serializer=SupportSerailizer(instance=support_help,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def support_helpDelete(request,pk):
    support_help=Support.objects.get(id=pk)
    support_help.delete()
    return JsonResponse("Deleted")

#21
from .models import Terms_Condition
from .serializers import Terms_ConditionSerailizer
@api_view(['GET'])
def term_conditionList(request):
    term_condition=Terms_Condition.objects.all()
    if term_condition is None:
        JsonResponse("No records")
    else:
      serializer=Terms_Condition(term_condition,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def term_conditionDetail(request,pk):
    term_condition=Terms_Condition.objects.get(id=pk)
    serializer=Terms_ConditionSerailizer(term_condition,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def term_conditionCreate(request):
    serializer=Terms_ConditionSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def term_conditionUpdate(request,pk):
    term_condition=Terms_Condition.objects.get(id=pk)
    serializer=Terms_ConditionSerailizer(instance=term_condition,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def term_conditionDelete(request,pk):
    term_condition=Terms_Condition.objects.get(id=pk)
    term_condition.delete()
    return JsonResponse("Deleted")

#22
from .models import Privacy_Policy
from .serializers import Privacy_PolicySerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def privacy_policyList(request):
    privacy_policy=Privacy_Policy.objects.all()
    if privacy_policy is None:
        JsonResponse("No records")
    else:
      serializer=Privacy_PolicySerailizer(privacy_policy,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def privacy_policyDetail(request,pk):
    privacy_policy=Privacy_Policy.objects.get(id=pk)
    serializer=Privacy_PolicySerailizer(privacy_policy,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def privacy_policyCreate(request):
    serializer=Privacy_PolicySerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def privacy_policyUpdate(request,pk):
    privacy_policy=Privacy_Policy.objects.get(id=pk)
    serializer=Privacy_PolicySerailizer(instance=privacy_policy,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def privacy_policyDelete(request,pk):
    privacy_policy=Privacy_Policy.objects.get(id=pk)
    privacy_policy.delete()
    return JsonResponse("Deleted")


#23
from .models import Vehicle_Monitoring
from .serializers import Vehicle_MonitoringSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def vehicle_monitoringList(request):
    vehicle_monitoring=Vehicle_Monitoring.objects.all()
    if vehicle_monitoring is None:
        JsonResponse("No records")
    else:
      serializer=Vehicle_MonitoringSerailizer(vehicle_monitoring,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def vehicle_monitoringDetail(request,pk):
    vehicle_monitoring=Vehicle_Monitoring.objects.get(id=pk)
    serializer=Vehicle_MonitoringSerailizer(vehicle_monitoring,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def vehicle_monitoringCreate(request):
    serializer=Vehicle_MonitoringSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def vehicle_monitoringUpdate(request,pk):
    vehicle_monitoring=Vehicle_Monitoring.objects.get(id=pk)
    serializer=Vehicle_MonitoringSerailizer(instance=vehicle_monitoring,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def vehicle_monitoringDelete(request,pk):
    vehicle_monitoring=Vehicle_Monitoring.objects.get(id=pk)
    vehicle_monitoring.delete()
    return JsonResponse("Deleted")


#24

from .models import List_your_vehicles_Management
from .serializers import List_your_vehicles_ManagementSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def list_your_vehicleList(request):
    list_your_vehicle=List_your_vehicles_Management.objects.all()
    if list_your_vehicle is None:
        JsonResponse("No records")
    else:
      serializer=List_your_vehicles_ManagementSerailizer(list_your_vehicle,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def list_your_vehicleDetail(request,pk):
    list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
    serializer=List_your_vehicles_ManagementSerailizer(list_your_vehicle,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def list_your_vehicleCreate(request):
    serializer=List_your_vehicles_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def list_your_vehicleUpdate(request,pk):
    list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
    serializer=List_your_vehicles_ManagementSerailizer(instance=list_your_vehicle,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def list_your_vehicleDelete(request,pk):
    list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
    list_your_vehicle.delete()
    return JsonResponse("Deleted")


#24

from .models import Listing_Management
from .serializers import Listing_ManagementSerailizer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def listingList(request):
    list_your_vehicle=Listing_Management.objects.all()
    if list_your_vehicle is None:
        JsonResponse("No records")
    else:
      serializer=Listing_ManagementSerailizer(list_your_vehicle,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def listingDetail(request,pk):
    list_your_vehicle=Listing_Management.objects.get(id=pk)
    serializer=Listing_ManagementSerailizer(list_your_vehicle,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def listingCreate(request):
    serializer=Listing_ManagementSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def listingUpdate(request,pk):
    list_your_vehicle=Listing_Management.objects.get(id=pk)
    serializer=Listing_ManagementSerailizer(instance=list_your_vehicle,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def listingDelete(request,pk):
    list_your_vehicle=Listing_Management.objects.get(id=pk)
    list_your_vehicle.delete()
    return JsonResponse("Deleted")