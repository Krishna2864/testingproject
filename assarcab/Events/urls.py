from . import views
from django.urls import path




urlpatterns=[

    path('adminlist/',views.adminList,name="admin_list"),
    path('admindetail/<int:id>/',views.adminDetail,name="admin_detail"),
    path('admincreate/',views.adminCreate,name="admin_create"),
    path('adminupdate/<int:id>/',views.adminUpdate,name="admin_update"),
    path('admindelete/<int:pk>/',views.adminDelete,name="admin_delete"),

#1
    path('userlist/',views.userList,name="user_list"),
    path('userdetail/<int:id>/',views.userDetail,name="user_detail"),
    path('usercreate/',views.userCreate,name="user_create"),
    path('userupdate/<int:id>/',views.userUpdate,name="user_update"),
    path('userdelete/<int:pk>/',views.userDelete,name="user_delete"),



#2


    path('vehiclelist/',views.vehicleList,name="vehicle_list"),
    path('vehicledetail/<int:id>/',views.vehicleDetail,name="vehicle_detail"),
    path('vehiclecreate/',views.vehicleCreate,name="vehicle_create"),
    path('vehicleupdate/<int:id>/',views.vehicleUpdate,name="vehicle_update"),
    path('vehicledelete/<int:pk>/',views.vehicleDelete,name="vehicle_delete"),

#3
    path('driverlist/',views.driverList,name="driver_list"),
    path('driverdetail/<int:id>/',views.driverDetail,name="driver_detail"),
    path('drivercreate/',views.driverCreate,name="driver_create"),
    path('driverupdate/<int:id>/',views.driverUpdate,name="driver_update"),
    path('driverdelete/<int:pk>/',views.driverDelete,name="driver_delete"),

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

    path('routelist/',views.routeList,name="route_list"),
    path('routedetail/<int:id>/',views.routeDetail,name="route_detail"),
    path('routecreate/',views.routeCreate,name="route_create"),
    path('routeupdate/<int:id>/',views.routeUpdate,name="route_update"),
    path('routedelete/<int:pk>/',views.routeDelete,name="route_delete"),

#13
    path('farelist/',views.fareList,name="fare_list"),
    path('faredetail/<int:id>/',views.fareDetail,name="fare_detail"),
    path('farecreate/',views.fareCreate,name="fare_create"),
    path('fareupdate/<int:id>/',views.fareUpdate,name="fare_update"),
    path('faredelete/<int:pk>/',views.fareDelete,name="fare_delete"),

    path('farelistoutstation/',views.farelistoutstation,name="fare_listt"),
    path('faredetailoutstation/<int:id>/',views.faredetailoutstation,name="fare_detail"),
    path('farecreateoutstation/',views.farecreateoutstation,name="fare_create"),
    path('fareupdateoutstation/<int:id>/',views.fareupdateoutstation,name="fare_update"),
    path('faredeleteoutstation/<int:pk>/',views.faredeleteoutstation,name="fare_delete"),

    path('farelistlocal/',views.farelistlocal,name="fare_list"),
    path('faredetaillocal/<int:id>/',views.faredetaillocal,name="fare_detail"),
    path('farecreatelocal/',views.farecreatelocal,name="fare_create"),
    path('fareupdatelocal/<int:id>/',views.fareupdatelocal,name="fare_update"),
    path('faredeletelocal/<int:pk>/',views.faredeletelocal,name="fare_delete"),
#14

    path('timeschedulelist/',views.time_scheduleList,name="time_schedule_list"),
    path('timescheduledetail/<int:id>/',views.time_scheduleDetail,name="time_schedule_detail"),
    path('timeschedulecreate/',views.time_scheduleCreate,name="time_schedule_create"),
    path('timescheduleupdate/<int:id>/',views.time_scheduleUpdate,name="time_schedule_update"),
    path('timescheduledelete/<int:pk>/',views.time_scheduleDelete,name="time_schedule_delete"),
#15
    path('pickuppointlist/',views.pickup_pointList,name="pickup_point_list"),
    path('pickuppointdetail/<int:id>/',views.pickup_pointDetail,name="pickup_point_detail"),
    path('pickuppointcreate/',views.pickup_pointCreate,name="pickup_point_create"),
    path('pickuppointupdate/<int:id>/',views.pickup_pointUpdate,name="pickup_point_update"),
    path('pickuppointdelete/<int:pk>/',views.pickup_pointDelete,name="pickup_point_delete"),
#16
    path('dropuppointlist/',views.dropup_pointList,name="dropup_point_list"),
    path('dropuppointdetail/<int:id>/',views.dropup_pointDetail,name="dropup_point_detail"),
    path('dropuppointcreate/',views.dropup_pointCreate,name="dropup_point_create"),
    path('dropuppointupdate/<int:id>/',views.dropup_pointUpdate,name="dropup_point_update"),
    path('dropuppointdelete/<int:pk>/',views.dropup_pointDelete,name="dropup_point_delete"),
#17

    path('listingassignlist/',views.listing_assignList,name="listing_assign_list"),
    path('listingassigndetail/<int:id>/',views.listing_assignDetail,name="listing_assign_detail"),
    path('listingassigncreate/',views.listing_assignCreate,name="listing_assign_create"),
    path('listingassignupdate/<int:id>/',views.listing_assignUpdate,name="listing_assign_update"),
    path('listingassigndelete/<int:pk>/',views.listing_assignDelete,name="listing_assign_delete"),

#18 
    path('copartnerlist/',views.co_partnerList,name="co_partner_list"),
    path('copartnerdetail/<int:id>/',views.co_partnerDetail,name="co_partner_detail"),
    path('copartnercreate/',views.co_partnerCreate,name="co_partner_create"),
    path('copartnerupdate/<int:id>/',views.co_partnerUpdate,name="co_partner_update"),
    path('copartnerdelete/<int:pk>/',views.co_partnerDelete,name="co_partner_delete"),

#19
    path('notificationtoridderlist/',views.notification_to_ridderList,name="notification_to_ridder_list"),
    path('notificationtoridderdetail/<int:id>/',views.notification_to_ridderDetail,name="notification_to_ridder_detail"),
    path('noticationtoriddercreate/',views.notification_to_ridderCreate,name="notification_to_ridder_create"),
    path('notificationtoridderupdate/<int:id>/',views.notification_to_ridderUpdate,name="notification_to_ridder_update"),
    path('notificationtoridderdelete/<int:pk>/',views.notification_to_ridderDelete,name="notification_to_ridder_delete"),

#20

    path('notificationtodriverlist/',views.notification_to_driverList,name="notification_to_driver_list"),
    path('notificationtodriverdetail/<int:id>/',views.notification_to_driverDetail,name="notification_to_driver_detail"),
    path('notificationtodrivercreate/',views.notification_to_driverCreate,name="notification_to_driver_create"),
    path('notificationtodriverupdate/<int:id>/',views.notification_to_driverUpdate,name="notification_to_driver_update"),
    path('notificationtodelete/<int:pk>/',views.notification_to_driverDelete,name="notification_to_driver_delete"),

#21
    path('consignmenttrackinglist/',views.consignment_trackingList,name="consignment_tracking_list"),
    path('consignmenttrackingdetail/<int:id>/',views.consignment_trackingDetail,name="consignment_tracking_detail"),
    path('consignmenttrackingcreate/',views.consignment_trackingCreate,name="consignment_tracking_create"),
    path('consignmenttrackingupdate/<int:id>/',views.consignment_trackingUpdate,name="consignment_tracking_update"),
    path('consignmenttrackingdelete/<int:pk>/',views.consignment_trackingDelete,name="consignment_tracking_delete"),

#22

    path('transactionlist/',views.transactionList,name="transaction_list"),
    path('transactiondetail/<int:id>/',views.transactionDetail,name="transaction_detail"),
    path('transactioncreate/',views.transactionCreate,name="transaction_create"),
    path('transactionupdate/<int:id>/',views.transactionUpdate,name="transaction_update"),
    path('transactiondelete/<int:pk>/',views.transactionDelete,name="transaction_delete"),

#23
    path('listyourvehiclelist/',views.list_your_vehicleList,name="list_your_vehicle_list"),
    path('listyourvehicledetail/<int:id>/',views.list_your_vehicleDetail,name="list_your_vehicle_detail"),
    path('listyourvehiclecreate/',views.list_your_vehicleCreate,name="list_your_vehicle_create"),
    path('listyourvehicleupdate/<int:id>/',views.list_your_vehicleUpdate,name="list_your_vehicle_update"),
    path('listyourvehicledelete/<int:pk>/',views.list_your_vehicleDelete,name="list_your_vehicle_delete"),
#24

    path('feedbacklist/',views.feedbackList,name="feedback_list"),
    path('feedbackdetail/<int:id>/',views.feedbackDetail,name="feedback_detail"),
    path('feedbackcreate/',views.feedbackCreate,name="feedback_create"),
    path('feedbackupdate/<int:id>/',views.feedbackUpdate,name="feedback_update"),
    path('feedbackdelete/<int:pk>/',views.feedbackDelete,name="feedback_delete"),

#25
    path('seatlist/',views.seatList,name="seat_list"),
    path('seatdetail/<int:id>/',views.seatDetail,name="seat_detail"),
    path('seatcreate/',views.seatCreate,name="seat_create"),
    path('seatupdate/<int:id>/',views.seatUpdate,name="seat_update"),
    path('seatdelete/<int:pk>/',views.seatDelete,name="seat_delete"),
#26
    path('soslist/',views.sosList,name="sos_list"),
    path('sosdetail/<int:id>/',views.sosDetail,name="sos_detail"),
    path('soscreate/',views.sosCreate,name="sos_create"),
    path('sosupdate/<int:id>/',views.sosUpdate,name="sos_update"),
    path('sosdelete/<int:pk>/',views.sosDelete,name="sos_delete"),

#27
    path('supportlist/',views.support_helpList,name="support_help_list"),
    path('supportdetail/<int:id>/',views.support_helpDetail,name="support_help_detail"),
    path('supportcreate/',views.support_helpCreate,name="support_help_create"),
    path('supportupdate/<int:id>/',views.support_helpUpdate,name="support_help_update"),
    path('supportdelete/<int:pk>/',views.support_helpDelete,name="support_help_delete"),
#28
 
    path('termconditionlist/',views.term_conditionList,name="term_condition_list"),
    path('termconditiondetail/<int:id>/',views.term_conditionDetail,name="term_condition_detail"),
    path('termconditioncreate/',views.term_conditionCreate,name="term_condition_create"),
    path('termconditionupdate/<int:id>/',views.term_conditionUpdate,name="term_condition_update"),
    path('termconditiondelete/<int:pk>/',views.term_conditionDelete,name="term_condition_delete"),

#29
    path('privacypolicylist/',views.privacy_policyList,name="privacy_policy_list"),
    path('privacypolicydetail/<int:id>/',views.privacy_policyDetail,name="privacy_policy_detail"),
    path('privacypolicycreate/',views.privacy_policyCreate,name="privacy_policy_create"),
    path('privacypolicyupdate/<int:id>/',views.privacy_policyUpdate,name="privacy_policy_update"),
    path('privacypolicydelete/<int:pk>/',views.privacy_policyDelete,name="privacy_policy_delete"),





   

]