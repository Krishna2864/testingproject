from . import views
from django.conf.urls import url
from django.urls import path, include
urlpatterns=[
#1
    path('adminlist/',views.adminList,name="admin_list"),
    path('admindetail/<int:id>/',views.adminDetail,name="admin_detail"),
    path('admincreate/',views.adminCreate,name="admin_create"),
    path('adminupdate/<int:id>/',views.adminUpdate,name="admin_update"),
    path('admindelete/<int:pk>/',views.adminDelete,name="admin_delete"),
#2
    path('userlist/',views.userList,name="user_list"),
    path('userdetail/<int:id>/',views.userDetail,name="user_detail"),
    path('usercreate/',views.userCreate,name="user_create"),
    path('userupdate/<int:id>/',views.userUpdate,name="user_update"),
    path('userdelete/<int:pk>/',views.userDelete,name="user_delete"),



#3
    path('vehiclelist/',views.vehicleList,name="vehicle_list"),
    path('vehicledetail/<int:id>/',views.vehicleDetail,name="vehicle_detail"),
    path('vehiclecreate/',views.vehicleCreate,name="vehicle_create"),
    path('vehicleupdate/<int:id>/',views.vehicleUpdate,name="vehicle_update"),
    path('vehicledelete/<int:pk>/',views.vehicleDelete,name="vehicle_delete"),



#4
    path('countrylist/',views.countryList,name="country_list"),
    path('countrydetail/<int:id>/',views.countryDetail,name="country_detail"),
    path('countrycreate/',views.countryCreate,name="country_create"),
    path('countryupdate/<int:id>/',views.countryUpdate,name="country_update"),
    path('countrydelete/<int:pk>/',views.countryDelete,name="country_delete"),

#5
    path('statelist/',views.stateList,name="state_list"),
    path('statedetail/<int:id>/',views.stateDetail,name="state_detail"),
    path('statecreate/',views.stateCreate,name="state_create"),
    path('stateupdate/<int:id>/',views.stateUpdate,name="state_update"),
    path('statedelete/<int:pk>/',views.stateDelete,name="state_delete"),

#6
    path('citylist/',views.cityList,name="city_list"),
    path('citydetail/<int:id>/',views.cityDetail,name="city_detail"),
    path('citycreate/',views.cityCreate,name="city_create"),
    path('cityupdate/<int:id>/',views.cityUpdate,name="city_update"),
    path('citydelete/<int:pk>/',views.cityDelete,name="city_delete"),


#7
    path('advertisementlist/',views.advertismentList,name="advertisement_list"),
    path('advertisementdetail/<int:id>/',views.advertismentDetail,name="advertisement_detail"),
    path('advertismentcreate/',views.advertismentCreate,name="advertisement_create"),
    path('advertisementupdate/<int:id>/',views.advertismentUpdate,name="advertisement_update"),
    path('advertisementdelete/<int:pk>/',views.advertismentDelete,name="advertisement_delete"),


#8
    path('refrallist/',views.refralList,name="refral_list"),
    path('refraldetail/<int:id>/',views.refralDetail,name="refral_detail"),
    path('refralcreate/',views.refralCreate,name="refral_create"),
    path('refralupdate/<int:id>/',views.refralUpdate,name="refral_update"),
    path('refraldelete/<int:pk>/',views.refralDelete,name="refral_delete"),

#9
    path('refundlist/',views.refundList,name="refund_list"),
    path('refunddetail/<int:id>/',views.refundDetail,name="refund_detail"),
    path('refundcreate/',views.refundCreate,name="refund_create"),
    path('refundupdate/<int:id>/',views.refundUpdate,name="refund_update"),
    path('refunddelete/<int:pk>/',views.refundDelete,name="refund_delete"),

#10
    path('fuellist/',views.fuelList,name="fuel_list"),
    path('fueldetail/<int:id>/',views.fuelDetail,name="fuel_detail"),
    path('fuelcreate/',views.fuelCreate,name="fuel_create"),
    path('fuelupdate/<int:id>/',views.fuelUpdate,name="fuel_update"),
    path('fueldelete/<int:pk>/',views.fuelDelete,name="fuel_delete"),


#11
    path('maintainancelist/',views.maintenanceList,name="maintenance_list"),
    path('maintainancedetail/<int:id>/',views.maintenanceDetail,name="maintenance_detail"),
    path('maintainancecreate/',views.maintenanceCreate,name="maintenance_create"),
    path('maintainanceupdate/<int:id>/',views.maintenanceUpdate,name="maintenance_update"),
    path('maintainancedelete/<int:pk>/',views.maintenanceDelete,name="maintenance_delete"),

#12
    path('farelist/',views.fareList,name="fare_list"),
    path('faredetail/<int:id>/',views.fareDetail,name="fare_detail"),
    path('farecreate/',views.fareCreate,name="fare_create"),
    path('fareupdate/<int:id>/',views.fareUpdate,name="fare_update"),
    path('faredelete/<int:pk>/',views.fareDelete,name="fare_delete"),

#13 
    path('copartnerlist/',views.co_partnerList,name="co_partner_list"),
    path('copartnerdetail/<int:id>/',views.co_partnerDetail,name="co_partner_detail"),
    path('copartnercreate/',views.co_partnerCreate,name="co_partner_create"),
    path('copartnerupdate/<int:id>/',views.co_partnerUpdate,name="co_partner_update"),
    path('copartnerdelete/<int:pk>/',views.co_partnerDelete,name="co_partner_delete"),

#14
    path('notificationtocopartnerlist/',views.notification_to_copartnerList,name="notification_to_copartner_list"),
    path('notificationtocopartnerdetail/<int:id>/',views.notification_to_copartnerDetail,name="notification_to_copartner_detail"),
    path('notificationtocopartnercreate/',views.notification_to_copartnerCreate,name="notification_to_copartner_create"),
    path('notificationtocopartnerupdate/<int:id>/',views.notification_to_copartnerUpdate,name="notification_to_copartner_update"),
    path('notificationtocopartnerrdelete/<int:pk>/',views.notification_to_copartnerDelete,name="notification_to_copartner_delete"),

#15

    path('notificationtouserlist/',views.notification_to_userList,name="notification_to_user_list"),
    path('notificationtouserdetail/<int:id>/',views.notification_to_userDetail,name="notification_to_user_detail"),
    path('notificationtousercreate/',views.notification_to_userCreate,name="notification_to_user_create"),
    path('notificationtouserupdate/<int:id>/',views.notification_to_userUpdate,name="notification_to_user_update"),
    path('notificationtouserdelete/<int:pk>/',views.notification_to_userDelete,name="notification_to_user_delete"),

#16
    path('contentlist/',views.contentList,name="content_list"),
    path('contentdetail/<int:id>/',views.contentDetail,name="content_detail"),
    path('contentcreate/',views.contentCreate,name="content_create"),
    path('contentupdate/<int:id>/',views.contentUpdate,name="content_update"),
    path('contentdelete/<int:pk>/',views.contentDelete,name="content_delete"),

#17

    path('transactionlist/',views.transactionList,name="transaction_list"),
    path('transactiondetail/<int:id>/',views.transactionDetail,name="transaction_detail"),
    path('transactioncreate/',views.transactionCreate,name="transaction_create"),
    path('transactionupdate/<int:id>/',views.transactionUpdate,name="transaction_update"),
    path('transactiondelete/<int:pk>/',views.transactionDelete,name="transaction_delete"),

#18
    path('listyourvehiclelist/',views.list_your_vehicleList,name="list_your_vehicle_list"),
    path('listyourvehicledetail/<int:id>/',views.list_your_vehicleDetail,name="list_your_vehicle_detail"),
    path('listyourvehiclecreate/',views.list_your_vehicleCreate,name="list_your_vehicle_create"),
    path('listyourvehicleupdate/<int:id>/',views.list_your_vehicleUpdate,name="list_your_vehicle_update"),
    path('listyourvehicledelete/<int:pk>/',views.list_your_vehicleDelete,name="list_your_vehicle_delete"),
#19

    path('feedbacklist/',views.feedbackList,name="feedback_list"),
    path('feedbackdetail/<int:id>/',views.feedbackDetail,name="feedback_detail"),
    path('feedbackcreate/',views.feedbackCreate,name="feedback_create"),
    path('feedbackupdate/<int:id>/',views.feedbackUpdate,name="feedback_update"),
    path('feedbackdelete/<int:pk>/',views.feedbackDelete,name="feedback_delete"),

#20
    path('soslist/',views.sosList,name="sos_list"),
    path('sosdetail/<int:id>/',views.sosDetail,name="sos_detail"),
    path('soscreate/',views.sosCreate,name="sos_create"),
    path('sosupdate/<int:id>/',views.sosUpdate,name="sos_update"),
    path('sosdelete/<int:pk>/',views.sosDelete,name="sos_delete"),

#21
    path('supportlist/',views.support_helpList,name="support_help_list"),
    path('supportdetail/<int:id>/',views.support_helpDetail,name="support_help_detail"),
    path('supportcreate/',views.support_helpCreate,name="support_help_create"),
    path('supportupdate/<int:id>/',views.support_helpUpdate,name="support_help_update"),
    path('supportdelete/<int:pk>/',views.support_helpDelete,name="support_help_delete"),
#22
 
    path('termconditionlist/',views.term_conditionList,name="term_condition_list"),
    path('termconditiondetail/<int:id>/',views.term_conditionDetail,name="term_condition_detail"),
    path('termconditioncreate/',views.term_conditionCreate,name="term_condition_create"),
    path('termconditionupdate/<int:id>/',views.term_conditionUpdate,name="term_condition_update"),
    path('termconditiondelete/<int:pk>/',views.term_conditionDelete,name="term_condition_delete"),

#23
    path('privacypolicylist/',views.privacy_policyList,name="privacy_policy_list"),
    path('privacypolicydetail/<int:id>/',views.privacy_policyDetail,name="privacy_policy_detail"),
    path('privacypolicycreate/',views.privacy_policyCreate,name="privacy_policy_create"),
    path('privacypolicyupdate/<int:id>/',views.privacy_policyUpdate,name="privacy_policy_update"),
    path('privacypolicydelete/<int:pk>/',views.privacy_policyDelete,name="privacy_policy_delete"),


#24
    path('listinglist/',views.listingList,name="listing_list"),
    path('listingdetail/<int:id>/',views.listingDetail,name="listing_detail"),
    path('listingcreate/',views.listingCreate,name="listing_create"),
    path('listingupdate/<int:id>/',views.listingUpdate,name="listing_update"),
    path('listingdelete/<int:pk>/',views.listingDelete,name="listing_delete"),


]