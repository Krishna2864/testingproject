from . import views
from django.conf.urls import url
from django.urls import path, include
#1
urlpatterns=[

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
    path('drivelist/',views.driveList,name="drive_list"),
    path('drivedetail/<int:id>/',views.driveDetail,name="drive_detail"),
    path('drivecreate/',views.driveCreate,name="drive_create"),
    path('driveupdate/<int:id>/',views.driveUpdate,name="drive_update"),
    path('drivedelete/<int:pk>/',views.driveDelete,name="drive_delete"),

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

#6
    path('city1list/',views.city1List,name="city1_list"),
    path('city1detail/<int:id>/',views.city1Detail,name="city1_detail"),
    path('city1create/',views.city1Create,name="city1_create"),
    path('city1update/<int:id>/',views.city1Update,name="city1_update"),
    path('city1delete/<int:pk>/',views.city1Delete,name="city1_delete"),


#7
    path('city_mlist/',views.city_mList,name="city_m_list"),
    path('city_mdetail/<int:id>/',views.city_mDetail,name="city_m_detail"),
    path('city_mcreate/',views.city_mCreate,name="city_m_create"),
    path('city_mupdate/<int:id>/',views.city_mUpdate,name="city_m_update"),
    path('city_mdelete/<int:pk>/',views.city_mDelete,name="city_m_delete"),


#8
    path('refrallist/',views.refralList,name="refral_list"),
    path('refraldetail/<int:id>/',views.refralDetail,name="refral_detail"),
    path('refralcreate/',views.refralCreate,name="refral_create"),
    path('refralupdate/<int:id>/',views.refralUpdate,name="refral_update"),
    path('refraldelete/<int:pk>/',views.refralDelete,name="refral_delete"),

#9
    path('fuellist/',views.fuelList,name="fuel_list"),
    path('fueldetail/<int:id>/',views.fuelDetail,name="fuel_detail"),
    path('fuelcreate/',views.fuelCreate,name="fuel_create"),
    path('fuelupdate/<int:id>/',views.fuelUpdate,name="fuel_update"),
    path('fueldelete/<int:pk>/',views.fuelDelete,name="fuel_delete"),

#10
    path('farelist/',views.fareList,name="fare_list"),
    path('faredetail/<int:id>/',views.fareDetail,name="fare_detail"),
    path('farecreate/',views.fareCreate,name="fare_create"),
    path('fareupdate/<int:id>/',views.fareUpdate,name="fare_update"),
    path('faredelete/<int:pk>/',views.fareDelete,name="fare_delete"),

#12
    path('outstationlist/',views.outstationList,name="outstation_list"),
    path('outstationdetail/<int:id>/',views.outstationDetail,name="outstation_detail"),
    path('outstationcreate/',views.outstationCreate,name="outstation_create"),
    path('outstationupdate/<int:id>/',views.outstationUpdate,name="outstation_update"),
    path('outstationdelete/<int:pk>/',views.outstationDelete,name="outstation_delete"),
#13
    path('outstationsecondlist/',views.outstation_sList,name="outstation_s_list"),
    path('outstationseconddetail/<int:id>/',views.outstation_sDetail,name="outstation_s_detail"),
    path('outstationsecondcreate/',views.outstation_sCreate,name="outstation_s_create"),
    path('outstationsecondupdate/<int:id>/',views.outstation_sUpdate,name="outstation_s_update"),
    path('outstationseconddelete/<int:pk>/',views.outstation_sDelete,name="outstation_s_delete"),

#14
    path('notificationtocustomerlist/',views.notification_to_customerList,name="notification_to_customer_list"),
    path('notificationtocustomerdetail/<int:id>/',views.notification_to_customerDetail,name="notification_to_customer_detail"),
    path('noticationtocustomercreate/',views.notification_to_customerCreate,name="notification_to_customer_create"),
    path('notificationtocustomerupdate/<int:id>/',views.notification_to_customerUpdate,name="notification_to_customer_update"),
    path('notificationtocustomerdelete/<int:pk>/',views.notification_to_customerDelete,name="notification_to_customer_delete"),

#15

    path('notificationtodriverlist/',views.notification_to_driverList,name="notification_to_driver_list"),
    path('notificationtodriverdetail/<int:id>/',views.notification_to_driverDetail,name="notification_to_driver_detail"),
    path('notificationtodrivercreate/',views.notification_to_driverCreate,name="notification_to_driver_create"),
    path('notificationtodriverupdate/<int:id>/',views.notification_to_driverUpdate,name="notification_to_driver_update"),
    path('notificationtodelete/<int:pk>/',views.notification_to_driverDelete,name="notification_to_driver_delete"),


#16

    path('transactionlist/',views.transactionList,name="transaction_list"),
    path('transactiondetail/<int:id>/',views.transactionDetail,name="transaction_detail"),
    path('transactioncreate/',views.transactionCreate,name="transaction_create"),
    path('transactionupdate/<int:id>/',views.transactionUpdate,name="transaction_update"),
    path('transactiondelete/<int:pk>/',views.transactionDelete,name="transaction_delete"),

#17
    path('listyourvehiclelist/',views.list_your_vehicleList,name="list_your_vehicle_list"),
    path('listyourvehicledetail/<int:id>/',views.list_your_vehicleDetail,name="list_your_vehicle_detail"),
    path('listyourvehiclecreate/',views.list_your_vehicleCreate,name="list_your_vehicle_create"),
    path('listyourvehicleupdate/<int:id>/',views.list_your_vehicleUpdate,name="list_your_vehicle_update"),
    path('listyourvehicledelete/<int:pk>/',views.list_your_vehicleDelete,name="list_your_vehicle_delete"),

#18
    path('soslist/',views.sosList,name="sos_list"),
    path('sosdetail/<int:id>/',views.sosDetail,name="sos_detail"),
    path('soscreate/',views.sosCreate,name="sos_create"),
    path('sosupdate/<int:id>/',views.sosUpdate,name="sos_update"),
    path('sosdelete/<int:pk>/',views.sosDelete,name="sos_delete"),

#19
    path('supportlist/',views.supportList,name="support_help_list"),
    path('supportdetail/<int:id>/',views.supportDetail,name="support_detail"),
    path('supportcreate/',views.supportCreate,name="support_create"),
    path('supportupdate/<int:id>/',views.supportUpdate,name="support_update"),
    path('supportdelete/<int:pk>/',views.supportDelete,name="support_delete"),
#20
 
    path('termconditionlist/',views.term_conditionList,name="term_condition_list"),
    path('termconditiondetail/<int:id>/',views.term_conditionDetail,name="term_condition_detail"),
    path('termconditioncreate/',views.term_conditionCreate,name="term_condition_create"),
    path('termconditionupdate/<int:id>/',views.term_conditionUpdate,name="term_condition_update"),
    path('termconditiondelete/<int:pk>/',views.term_conditionDelete,name="term_condition_delete"),

#21
    path('privacypolicylist/',views.privacy_policyList,name="privacy_policy_list"),
    path('privacypolicydetail/<int:id>/',views.privacy_policyDetail,name="privacy_policy_detail"),
    path('privacypolicycreate/',views.privacy_policyCreate,name="privacy_policy_create"),
    path('privacypolicyupdate/<int:id>/',views.privacy_policyUpdate,name="privacy_policy_update"),
    path('privacypolicydelete/<int:pk>/',views.privacy_policyDelete,name="privacy_policy_delete"),

#22
    path('dashboardlist/',views.dashboardList,name="dashboard_list"),
    path('dashboarddetail/<int:id>/',views.dashboardDetail,name="dashboard_detail"),
    path('dashboardcreate/',views.dashboardCreate,name="dashboard_create"),
    path('dashboardupdate/<int:id>/',views.dashboardUpdate,name="dashboard_update"),
    path('dashboarddelete/<int:pk>/',views.dashboardDelete,name="dashboard_delete"),

#18
    path('manitainancelist/',views.maintainanceList,name="maintainance_list"),
    path('maintainancedetail/<int:id>/',views.maintainanceDetail,name="maintainance_detail"),
    path('maintainancecreate/',views.maintainanceCreate,name="maintainace_create"),
    path('maintainanceupdate/<int:id>/',views.maintainanceUpdate,name="maintainance_update"),
    path('maintainancedelete/<int:pk>/',views.maintainanceDelete,name="maintainance_delete"),

#18
    path('advertismentlist/',views.advertismentList,name="advertisment_list"),
    path('advertismentdetail/<int:id>/',views.advertismentDetail,name="advertisment_detail"),
    path('advertismentcreate/',views.advertismentCreate,name="advertisment_create"),
    path('advertismentupdate/<int:id>/',views.advertismentUpdate,name="advertisment_update"),
    path('advertismentdelete/<int:pk>/',views.advertismentDelete,name="advertisment_delete"),

#18
    path('listinglist/',views.listingList,name="listing_list"),
    path('listingdetail/<int:id>/',views.listingDetail,name="listing_detail"),
    path('listingcreate/',views.listingCreate,name="listing_create"),
    path('listingupdate/<int:id>/',views.listingUpdate,name="listing_update"),
    path('listingdelete/<int:pk>/',views.listingDelete,name="listing_delete"),

#18
    path('vehiclelist/',views.vehicleList,name="vehicle_list"),
    path('vehicledetail/<int:id>/',views.vehicleDetail,name="vehicle_detail"),
    path('vehiclecreate/',views.vehicleCreate,name="vehicle_create"),
    path('vehicleupdate/<int:id>/',views.vehicleUpdate,name="vehicle_update"),
    path('vehicledelete/<int:pk>/',views.vehicleDelete,name="vehicle_delete"),


#23
    path('templatelist/',views.templateList,name="template_list"),
    path('templatedetail/<int:id>/',views.templateDetail,name="template_detail"),
    path('templatecreate/',views.templateCreate,name="template_create"),
    path('templateupdate/<int:id>/',views.templateUpdate,name="template_update"),
    path('templatedelete/<int:pk>/',views.templateDelete,name="template_delete"),


#24
    path('copartnerlist/',views.co_partnerList,name="co_partnerlist"),
    path('copartnerdetail/<int:id>/',views.co_partnerDetail,name="co_partner_detail"),
    path('copartnercreate/',views.co_partnerCreate,name="co_partner_create"),
    path('copartnerupdate/<int:id>/',views.co_partnerUpdate,name="co_partner_update"),
    path('copartnerdelete/<int:pk>/',views.co_partnerDelete,name="cp_partner_delete"),



]
