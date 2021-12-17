from . import views
from django.conf.urls import url
from django.urls import path, include
#0
urlpatterns=[

#1


    path('vehiclelist/',views.vehicleList,name="vehicle_list"),
    path('vehicledetail/<int:id>/',views.vehicleDetail,name="vehicle_detail"),
    path('vehiclecreate/',views.vehicleCreate,name="vehicle_create"),
    path('vehicleupdate/<int:id>/',views.vehicleUpdate,name="vehicle_update"),
    path('vehicledelete/<int:pk>/',views.vehicleDelete,name="vehicle_delete"),

#2
    path('driverlist/',views.driverList,name="driver_list"),
    path('driverdetail/<int:id>/',views.driverDetail,name="driver_detail"),
    path('drivercreate/',views.driverCreate,name="driver_create"),
    path('driverupdate/<int:id>/',views.driverUpdate,name="driver_update"),
    path('driverdelete/<int:pk>/',views.driverDelete,name="driver_delete"),

#3
    path('countrylist/',views.countryList,name="country_list"),
    path('countrydetail/<int:id>/',views.countryDetail,name="country_detail"),
    path('countrycreate/',views.countryCreate,name="country_create"),
    path('countryupdate/<int:id>/',views.countryUpdate,name="country_update"),
    path('countrydelete/<int:pk>/',views.countryDelete,name="country_delete"),

#4
    path('statelist/',views.stateList,name="state_list"),
    path('statedetail/<int:id>/',views.stateDetail,name="state_detail"),
    path('statecreate/',views.stateCreate,name="state_create"),
    path('stateupdate/<int:id>/',views.stateUpdate,name="state_update"),
    path('statedelete/<int:pk>/',views.stateDelete,name="state_delete"),

#5
    path('citylist/',views.cityList,name="city_list"),
    path('citydetail/<int:id>/',views.cityDetail,name="city_detail"),
    path('citycreate/',views.cityCreate,name="city_create"),
    path('cityupdate/<int:id>/',views.cityUpdate,name="city_update"),
    path('citydelete/<int:pk>/',views.cityDelete,name="city_delete"),


#6
    path('advertisementlist/',views.advertismentList,name="advertisement_list"),
    path('advertisementdetail/<int:id>/',views.advertismentDetail,name="advertisement_detail"),
    path('advertismentcreate/',views.advertismentCreate,name="advertisement_create"),
    path('advertisementupdate/<int:id>/',views.advertismentUpdate,name="advertisement_update"),
    path('advertisementdelete/<int:pk>/',views.advertismentDelete,name="advertisement_delete"),


#7
    path('refrallist/',views.refralList,name="refral_list"),
    path('refraldetail/<int:id>/',views.refralDetail,name="refral_detail"),
    path('refralcreate/',views.refralCreate,name="refral_create"),
    path('refralupdate/<int:id>/',views.refralUpdate,name="refral_update"),
    path('refraldelete/<int:pk>/',views.refralDelete,name="refral_delete"),

#8
    path('fuellist/',views.fuelList,name="fuel_list"),
    path('fueldetail/<int:id>/',views.fuelDetail,name="fuel_detail"),
    path('fuelcreate/',views.fuelCreate,name="fuel_create"),
    path('fuelupdate/<int:id>/',views.fuelUpdate,name="fuel_update"),
    path('fueldelete/<int:pk>/',views.fuelDelete,name="fuel_delete"),


#9
    path('maintainancelist/',views.maintenanceList,name="maintenance_list"),
    path('maintainancedetail/<int:id>/',views.maintenanceDetail,name="maintenance_detail"),
    path('maintainancecreate/',views.maintenanceCreate,name="maintenance_create"),
    path('maintainanceupdate/<int:id>/',views.maintenanceUpdate,name="maintenance_update"),
    path('maintainancedelete/<int:pk>/',views.maintenanceDelete,name="maintenance_delete"),

#10
    path('farelist/',views.fareList,name="fare_list"),
    path('faredetail/<int:id>/',views.fareDetail,name="fare_detail"),
    path('farecreate/',views.fareCreate,name="fare_create"),
    path('fareupdate/<int:id>/',views.fareUpdate,name="fare_update"),
    path('faredelete/<int:pk>/',views.fareDelete,name="fare_delete"),

#11

    path('listinlist/',views.listingList,name="listing_list"),
    path('listingdetail/<int:id>/',views.listingDetail,name="listing_detail"),
    path('listingcreate/',views.listingCreate,name="listing_create"),
    path('listingupdate/<int:id>/',views.listingUpdate,name="listing_update"),
    path('listingdelete/<int:pk>/',views.listingDelete,name="listing_delete"),

#12 
    path('copartnerlist/',views.co_partnerList,name="co_partner_list"),
    path('copartnerdetail/<int:id>/',views.co_partnerDetail,name="co_partner_detail"),
    path('copartnercreate/',views.co_partnerCreate,name="co_partner_create"),
    path('copartnerupdate/<int:id>/',views.co_partnerUpdate,name="co_partner_update"),
    path('copartnerdelete/<int:pk>/',views.co_partnerDelete,name="co_partner_delete"),


#13

    path('notificationtodriverlist/',views.notification_to_driverList,name="notification_to_driver_list"),
    path('notificationtodriverdetail/<int:id>/',views.notification_to_driverDetail,name="notification_to_driver_detail"),
    path('notificationtodrivercreate/',views.notification_to_driverCreate,name="notification_to_driver_create"),
    path('notificationtodriverupdate/<int:id>/',views.notification_to_driverUpdate,name="notification_to_driver_update"),
    path('notificationtodelete/<int:pk>/',views.notification_to_driverDelete,name="notification_to_driver_delete"),


#14

    path('transactionlist/',views.transactionList,name="transaction_list"),
    path('transactiondetail/<int:id>/',views.transactionDetail,name="transaction_detail"),
    path('transactioncreate/',views.transactionCreate,name="transaction_create"),
    path('transactionupdate/<int:id>/',views.transactionUpdate,name="transaction_update"),
    path('transactiondelete/<int:pk>/',views.transactionDelete,name="transaction_delete"),

#15
    path('listyourvehiclelist/',views.list_your_vehicleList,name="list_your_vehicle_list"),
    path('listyourvehicledetail/<int:id>/',views.list_your_vehicleDetail,name="list_your_vehicle_detail"),
    path('listyourvehiclecreate/',views.list_your_vehicleCreate,name="list_your_vehicle_create"),
    path('listyourvehicleupdate/<int:id>/',views.list_your_vehicleUpdate,name="list_your_vehicle_update"),
    path('listyourvehicledelete/<int:pk>/',views.list_your_vehicleDelete,name="list_your_vehicle_delete"),
#16

    path('feedbacklist/',views.feedbackList,name="feedback_list"),
    path('feedbackdetail/<int:id>/',views.feedbackDetail,name="feedback_detail"),
    path('feedbackcreate/',views.feedbackCreate,name="feedback_create"),
    path('feedbackupdate/<int:id>/',views.feedbackUpdate,name="feedback_update"),
    path('feedbackdelete/<int:pk>/',views.feedbackDelete,name="feedback_delete"),
 
#17
    path('termconditionlist/',views.term_conditionList,name="term_condition_list"),
    path('termconditiondetail/<int:id>/',views.term_conditionDetail,name="term_condition_detail"),
    path('termconditioncreate/',views.term_conditionCreate,name="term_condition_create"),
    path('termconditionupdate/<int:id>/',views.term_conditionUpdate,name="term_condition_update"),
    path('termconditiondelete/<int:pk>/',views.term_conditionDelete,name="term_condition_delete"),

#18
    path('privacypolicylist/',views.privacy_policyList,name="privacy_policy_list"),
    path('privacypolicydetail/<int:id>/',views.privacy_policyDetail,name="privacy_policy_detail"),
    path('privacypolicycreate/',views.privacy_policyCreate,name="privacy_policy_create"),
    path('privacypolicyupdate/<int:id>/',views.privacy_policyUpdate,name="privacy_policy_update"),
    path('privacypolicydelete/<int:pk>/',views.privacy_policyDelete,name="privacy_policy_delete"),


#18
    path('outstationlist/',views.outstationList,name="privacy_policy_list"),
    path('outstationdetail/<int:id>/',views.outstationDetail,name="privacy_policy_detail"),
    path('outstationcreate/',views.outstationCreate,name="privacy_policy_create"),
    path('outstationupdate/<int:id>/',views.outstationUpdate,name="privacy_policy_update"),
    path('outstationdelete/<int:pk>/',views.outstationDelete,name="privacy_policy_delete"),

]
