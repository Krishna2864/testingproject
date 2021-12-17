from django.db import models

# models 


# Event admin model

class Admin_Management(models.Model):
    s_no=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    name=models.CharField(max_length=80,null=True)
    username=models.CharField(max_length=80,null=True)
    email_id=models.EmailField(max_length=254,unique=True)
    mobile_no=models.IntegerField(null=True)
    option=models.CharField(max_length=80,null=True)
    listview=models.CharField(max_length=80,null=True)
    set_permission=models.BooleanField(default=False)
    set_permission_co_partner=models.BooleanField(default=False)
    set_permission_country=models.BooleanField(default=False)
    set_permission_state=models.BooleanField(default=False)
    set_permission_advertisement=models.BooleanField(default=False)
    set_permission_listing=models.BooleanField(default=False)
    set_permission_Templates=models.BooleanField(default=False)
    set_permission_fare=models.BooleanField(default=False)
    set_permission_notification=models.BooleanField(default=False)
    set_permission_notification2=models.BooleanField(default=False)
    set_permission_fuel=models.BooleanField(default=False)
    set_permission_maintainance=models.BooleanField(default=False)
    set_permission_refral=models.BooleanField(default=False)
    set_permission_refund=models.BooleanField(default=False)
    set_permission_trasaction=models.BooleanField(default=False)
    set_permission_feedback=models.BooleanField(default=False)
    set_permission_sos=models.BooleanField(default=False)
    set_permission_support=models.BooleanField(default=False)
    set_permission_other=models.BooleanField(default=False)

# user model

class User_Management(models.Model):
    booking_id=models.CharField(max_length=80,null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    no_of_passanger=models.IntegerField(null=True)
    name=models.CharField(max_length=80,null=True)
    username=models.CharField(max_length=80,null=True)
    email_id=models.EmailField(max_length=254,unique=True)
    mobile_no=models.IntegerField(null=True)
    booking_status=models.CharField(max_length=80,null=True)
    booking_status_1=models.CharField(max_length=80,null=True)
    booking_created=models.DateTimeField(auto_now=True)
    pickup_point=models.CharField(max_length=80,null=True)
    drop_p_point=models.CharField(max_length=80,null=True)
    sta=models.DateTimeField(auto_now=True)
    std=models.DateTimeField(auto_now=True)
    pickup_late_log=models.FloatField(null=True)
    drop_late_log=models.FloatField(null=True)
    ete_in_min= models.IntegerField(null=True)
    map_view=models.CharField(max_length=80,null=True)
    passanger_detail=models.CharField(max_length=150,null=True)
    vehicle_no=models.CharField(max_length=80,null=True)
    driver_id=models.CharField(max_length=80,null=True)
    driver_name=models.CharField(max_length=80,null=True)
    sos_or_help=models.CharField(max_length=80,null=True)
    base_fare=models.IntegerField(null=True)
    gst=models.IntegerField(null=True)
    booking_fee=models.IntegerField(null=True)
    commision_fee=models.IntegerField(null=True)
    per_min_charge=models.IntegerField(null=True)
    gst=models.IntegerField(null=True)

    insurance=models.IntegerField(null=True)
    extra_km=models.IntegerField(null=True)
    waiting_charge=models.IntegerField(null=True)
    night_charge=models.IntegerField(null=True)
    driver_charge=models.IntegerField(null=True)


    discount=models.IntegerField(null=True)
    minimum_bill=models.IntegerField(null=True)
    final_bill=models.IntegerField(null=True)
    invoice=models.ImageField(upload_to="media",null=True)
    pay_mode=models.CharField(max_length=80,null=True)
    


class Vehicle_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=True)
    s_no=models.IntegerField(null=True)
    vehicle_registration_no=models.CharField(max_length=80,null=True)
    manufacturer=models.CharField(max_length=80,null=True)
    year_of_manufacturing=models.IntegerField(null=True)
    engine_no=models.CharField(max_length=80,null=True)
    chassis_no=models.CharField(max_length=80,null=True)
    colour=models.CharField(max_length=80,null=True)
    seat_capa=models.IntegerField(null=True)
    segment=models.ImageField(upload_to="media",null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    varient=models.CharField(max_length=80,null=True)
    km_running=models.IntegerField(null=True)
    insurance=models.ImageField(upload_to="media",null=True)
    rc_card=models.ImageField(upload_to="media",null=True)
    fitness=models.ImageField(upload_to="media",null=True)
    permit=models.ImageField(upload_to="media",null=True)
    puc=models.ImageField(upload_to="media",null=True)
    date_of_attachment=models.DateField(auto_now=True)
    city=models.CharField(max_length=80,null=True)
    status=models.CharField(max_length=80,null=True)



class Driver_Mangement(models.Model):
    driver_id=models.CharField(max_length=80,null=True)
    vehicle_no=models.CharField(max_length=80,null=True)
    segment=models.CharField(max_length=80,null=True)
    dl=models.ImageField(upload_to="media",null=True)
    selfie=models.ImageField(upload_to="media",null=True)
    aadhar=models.ImageField(upload_to="media",null=True)
    pan_card=models.ImageField(upload_to="media",null=True)
    electric_bill=models.ImageField(upload_to="media",null=True)
    role=models.CharField(max_length=80,null=True)
    mobile_no=models.IntegerField(null=True)
    dl_expiry_date=models.DateField(auto_now=True)
    status=models.CharField(max_length=80,null=True)
    shift=models.CharField(max_length=80,null=True)
    police_verfication=models.CharField(max_length=80,null=True)
    driver_app_login=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=80,null=True)
    forgot_password=models.CharField(max_length=80,null=True)



class Country_Management(models.Model):
    s_no=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    start_date=models.DateField(auto_now=True)
    office_address=models.CharField(max_length=200,null=True)
    office_contact_no=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)


class State_Management(models.Model):
    s_no=models.IntegerField(null=True)
    state=models.CharField(max_length=80,null=True)
    start_date=models.DateField(auto_now=True)
    office_address=models.CharField(max_length=200,null=True)
    office_contact_no=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)



class City_Management(models.Model):
    s_no=models.IntegerField(null=True)
    city=models.CharField(max_length=80,null=True)
    start_date=models.DateField(auto_now=True)
    office_address=models.CharField(max_length=200,null=True)
    office_contact_no=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)


class Advertisement_Management(models.Model):
    s_no=models.IntegerField(null=True)
    Promo_code_name=models.CharField(max_length=80,null=True)
    promo_code=models.CharField(max_length=80,null=True)
    vehicle=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    valid_from=models.DateField(auto_now=True)
    valid_upto=models.DateField(auto_now=True)
    status_code=models.CharField(max_length=80,null=True)
    discount_type=models.IntegerField(null=True)
    user_type=models.CharField(max_length=80,null=True)
    discount_value= models.IntegerField(null=True)


class Refral_Mangemnt(models.Model):
    refral_content=models.CharField(max_length=80,null=True)
    refral_amount=models.IntegerField(null=True)
    refral_code=models.CharField(max_length=80,null=True)
    expiry_date=models.DateField(auto_now=True)
    start_date=models.DateField(auto_now=True)
    refral_image=models.IntegerField(null=True)
    no_user_used_code=models.IntegerField(null=True)


class Refund_Management(models.Model):
    s_no=models.IntegerField(null=True)
    booking_id=models.CharField(max_length=80,null=True)
    gst_amount=models.IntegerField(null=True)
    gateway_charges_amount=models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    cancellation_charges=models.IntegerField(null=True)
    booking_amount=models.IntegerField(null=True)
    total_refund_amount=models.IntegerField(null=True)
    date_of_refounded=models.IntegerField(null=True)
    mode=models.CharField(max_length=80,null=True)
    transaction_id=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)


class Fuel_Mangement(models.Model):
    total_cunsumption_inr=models.IntegerField(null=True)
    diesel_cunsumption=models.IntegerField(null=True)
    petrol_cunsumption=models.IntegerField(null=True)
    cnc_cunsumption=models.IntegerField(null=True)
    cng_cunsumption=models.IntegerField(null=True)
    lpg_cunsumption=models.IntegerField(null=True)
    electri=models.IntegerField(null=True)


class Maintenance_Management(models.Model):
    s_no=models.IntegerField(null=True)
    vehicle_no=models.CharField(max_length=80,null=True)
    date_of_services=models.DateField(auto_now=True)
    next_due_date_of_services=models.DateTimeField(auto_now=True)
    ruuning_km=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)
    tyure_replace=models.DateField(auto_now=True)
    spare_per_invoice=models.ImageField(upload_to="media",null=True)
    insurance_claim=models.ImageField(upload_to="media",null=True)


class Templates_Management(models.Model):
    s_no=models.IntegerField(null=True)
    booking_confirmation=models.CharField(max_length=150,null=True)
    for_varification=models.CharField(max_length=150,null=True)
    reset_password=models.CharField(max_length=100,null=True)
    booking_cancel_sms=models.CharField(max_length=150,null=True)


class Fare_Management(models.Model):
    vehicle_type=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    fuel_status=models.CharField(max_length=80,null=True)
    trip_type=models.CharField(max_length=80,null=True)
    
class Fare_Management_Outstation(models.Model):
    vehicle_type=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    fuel_status=models.CharField(max_length=80,null=True)
    trip_type=models.CharField(max_length=80,null=True)


class Fare_Management_Local(models.Model):
    vehicle_type=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    fuel_status=models.CharField(max_length=80,null=True)
    trip_type=models.CharField(max_length=80,null=True)
    




class Listing_Manangement(models.Model):
    vehicle_type=models.CharField(max_length=80,null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    fuel_status=models.CharField(max_length=80,null=True)
    booking_cat=models.IntegerField(null=True)
    v_id=models.CharField(max_length=80,null=True)
    setment=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    base_fare=models.IntegerField(null=True)
    booking_fee=models.IntegerField(null=True)
    commision_fee=models.IntegerField(null=True)
    per_min_charge=models.IntegerField(null=True)
    per_km_charge=models.IntegerField(null=True)
    minimum_bill=models.IntegerField(null=True)
    tool_tax=models.IntegerField(null=True)
    parking=models.IntegerField(null=True)
    seat=models.IntegerField(null=True)
    image=models.ImageField(upload_to="media",null=True)
    edit_button=models.CharField(max_length=80,null=True)
    listing=models.CharField(max_length=80,null=True)

    
class Route_Management(models.Model):
    s_no=models.IntegerField(null=True)
    state=models.CharField(max_length=80,null=True)
    _from=models.CharField(max_length=80,null=True)
    _to=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)


class Fare_Management(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    window_fare=models.FloatField(null=True)
    middle_seat_fare=models.FloatField(null=True)
    gst=models.FloatField(null=True)
    insurance=models.FloatField(null=True)
    fare_per_seat_window=models.IntegerField(null=True)
    middle_seat=models.IntegerField(null=True)
    option=models.CharField(max_length=80,null=True)



class TIME_SCHEDULE_MGMT(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    sdt=models.DateTimeField(auto_now=True)
    sat=models.DateTimeField
    state=models.CharField(max_length=80,null=True)
    _from=models.CharField(max_length=80,null=True)
    _to=models.CharField(max_length=80,null=True)
    frequency=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)

class Pickup_Point_Management(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    pickup=models.CharField(max_length=80,null=True)
    interval_min=models.IntegerField(null=True)
    lat=models.IntegerField(null=True)
    log=models.IntegerField(null=True)
    model=models.CharField(max_length=80,null=True)
    fuel=models.CharField(max_length=80,null=True)


class DROPUp_Point_Management(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    drop_point=models.CharField(max_length=80,null=True)
    interval_min=models.IntegerField(null=True)
    lat=models.IntegerField(null=True)
    log=models.IntegerField(null=True)
    model=models.CharField(max_length=80,null=True)
    fuel=models.CharField(max_length=80,null=True)



class Listing_ASSIGN_Management(models.Model):
    s_no=models.IntegerField(null=True)
    country=models.CharField(max_length=80,null=True)
    state=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    sdt=models.DateTimeField(auto_now=True)
    sat=models.DateTimeField(auto_now=True)
    vehicle_no=models.CharField(max_length=80,null=True)
    manufacturer=models.CharField(max_length=80,null=True)
    vehicle=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    driver=models.CharField(max_length=80,null=True)
    mobile_no=models.IntegerField(null=True)

class Co_partner_Management(models.Model):
    s_no=models.IntegerField(null=True)
    vehicle_registration_no=models.CharField(max_length=80,null=True)
    selfie=models.ImageField(upload_to="media",null=True)
    ower_name= models.CharField(max_length=80,null=True)
    aadhar_card=models.ImageField(upload_to="media",null=True)
    pan_card=models.ImageField(upload_to="media",null=True)
    bank_details=models.ImageField(upload_to="media",null=True)
    vehicle_type=models.CharField(max_length=80,null=True)
    mobile_no=models.IntegerField(null=True)
    email_id=models.EmailField(max_length=254,unique=True)
    payout_day=models.IntegerField(null=True)
    payout_month=models.IntegerField(null=True)
    online_total_time_in_hour=models.IntegerField(null=True)
    payout=models.CharField(max_length=80,null=True)


class Notification_to_Ridder(models.Model):
    pass


class Notification_to_Driver(models.Model):
    pass


class Consignment_Tracking(models.Model):
    s_no=models.IntegerField(null=True)
    sender_name=models.CharField(max_length=80,null=True)
    sender_no=models.IntegerField(null=True)
    address=models.CharField(max_length=200,null=True)
    email_id=models.EmailField(max_length=254,unique=True)
    weight=models.IntegerField(null=True)
    reciever_name=models.CharField(max_length=80,null=True)
    reciever_no=models.IntegerField(null=True)
    type=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    ##uid=


class Transaction_Management(models.Model):
    s_no=models.IntegerField(null=True)
    booking_id=models.CharField(max_length=80,null=True)
    #no_of_passanger=models.IntegerField(null=True)
    #date_of_join=models.DateField(auto_now=True)
    #booking_created=models.DateField(auto_now=True)
    gst_amount=models.IntegerField(null=True)
    gateway_charges_amount=models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    discount=models.IntegerField(null=True)
    segment= models.CharField(max_length=100)
    base_fare=models.IntegerField(null=True)
    booking_fee=models.IntegerField(null=True)
    commision_fee=models.IntegerField(null=True)
    per_min_charge=models.IntegerField(null=True)
    per_km_charge=models.IntegerField(null=True)
    gst=models.IntegerField(null=True)
    insurance=models.IntegerField(null=True)
    extra_km=models.IntegerField(null=True)
    waiting_charge=models.IntegerField(null=True)
    night_charge=models.IntegerField(null=True)
    discount=models.IntegerField(null=True)
    minimum_bill=models.IntegerField(null=True)
    final_bill=models.IntegerField(null=True)
    payment_mode=models.CharField(max_length=80,null=True)
    invoice=models.ImageField(upload_to="media",null=True)



class LIST_YOUR_VEHICLE_MGMT(models.Model):
    vehicle=models.CharField(max_length=80,null=True)
    s_no=models.IntegerField(null=True)
    vehicle_registration_no=models.CharField(max_length=80,null=True)
    manufacturer=models.CharField(max_length=80,null=True)
    year_of_manufacturing=models.IntegerField(null=True)
    engine_no_tracing=models.ImageField(upload_to="media",null=True)
    chassis_no_tracing=models.ImageField(upload_to="media",null=True)
    colour=models.CharField(max_length=80,null=True)
    seat_capa=models.IntegerField(null=True)
    segment=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    varient=models.CharField(max_length=80,null=True)
    km_running=models.IntegerField(null=True)
    insurance=models.ImageField(upload_to="media",null=True)
    rc_card=models.ImageField(upload_to="media",null=True)
    fitness=models.ImageField(upload_to="media",null=True)
    permit=models.ImageField(upload_to="media",null=True)
    puc=models.ImageField(upload_to="media",null=True)
    date_of_inspection=models.DateField(auto_now=True)
    proposed_price_day=models.CharField(max_length=80,null=True)
    proposed_price_night=models.CharField(max_length=80,null=True)
    proposed_date_of_attachment=models.DateField(auto_now=True)
    city=models.CharField(max_length=80,null=True)
    selfie=models.ImageField(upload_to="media",null=True)
    Ower_name=models.CharField(max_length=80,null=True)
    aadhar_card=models.ImageField(upload_to='media',null=True)
    pan_card=models.ImageField(upload_to="media",null=True)
    bank_details=models.ImageField(upload_to="media",null=True)
    mobile_no=models.IntegerField(null=True)
    mail_id=models.EmailField(max_length=254,unique=True)
    payout_hourly=models.IntegerField(null=True)
    payout_daily=models.IntegerField(null=True)


class Feedback(models.Model):
    pass


class Seat_Mangement(models.Model):
    s_no=models.IntegerField(null=True)
    employee_id=models.CharField(max_length=80,null=True)
    name=models.CharField(max_length=80,null=True)
    customer_name=models.CharField(max_length=80,null=True)
    gender=models.CharField(max_length=80,null=True)
    age=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    time=models.DateTimeField(auto_now=True)
    date=models.DateField(auto_now=True)
    From=models.CharField(max_length=80,null=True)
    to=models.CharField(max_length=80,null=True)
    seat_no=models.CharField(max_length=80,null=True)
    pickup_point=models.CharField(max_length=80,null=True)
    pickup_time=models.CharField(max_length=80,null=True)
    drop_point=models.CharField(max_length=80,null=True)
    drop_time=  models.DateTimeField(auto_now=True)


class SOS(models.Model):
    pass


class Support_HELP(models.Model):
    pass


class TERMS_CONDITIONS(models.Model):
    pass


class PRIVACY_POLICY(models.Model):
    pass
