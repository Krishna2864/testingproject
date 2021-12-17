from django.db import models
# Create your models here.
class DashBoard(models.Model):
    pass

class Admin_Management(models.Model):
    s_no=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    name=models.CharField(max_length=80,null=False)
    username=models.CharField(max_length=80,null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    mobile_no=models.IntegerField()
    option=models.CharField(max_length=80,null=False)
    listview=models.CharField(max_length=80,null=False)
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


class User_Management(models.Model):
    booking_id=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    name=models.CharField(max_length=80,null=False)
    username=models.CharField(max_length=80,null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    mobile_no=models.IntegerField()
    booking_status=models.CharField(max_length=80,null=False)
    booking_cat=models.CharField(max_length=80,null=False)
    booking_status_1=models.CharField(max_length=80,null=False)
    booking_created=models.DateTimeField(auto_now_add=True)
    pickup_point=models.CharField(max_length=80,null=False)
    drop_p_point=models.CharField(max_length=80,null=False)
    eta_in_min=models.IntegerField()
    et_time_in_min=models.IntegerField()
    etc_inr=models.IntegerField()
    actual_pickup_point=models.CharField(max_length=80,null=False)
    actual_drop_point=models.CharField(max_length=80,null=False)
    etkm_in_km=models.IntegerField()
    pickup_late_log=models.FloatField()
    drop_late_log=models.FloatField()
    doj=models.DateTimeField(auto_now_add=True)
    dod=models.DateTimeField(auto_now_add=True)
    actual_km_run=models.IntegerField
    vehicle_no=models.CharField(max_length=80,null=False)
    driver_id=models.CharField(max_length=80,null=False)
    driver_name=models.CharField(max_length=80,null=False)
    map_view=models.CharField(max_length=80,null=False)
    sos_or_help=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    gst= models.IntegerField()
    insurance=models.IntegerField()
    extra_km=models.IntegerField()
    waitng_charge=models.IntegerField()
    night_charge=models.IntegerField()
    driver_charge=models.IntegerField()
    discount=models.IntegerField()
    minimum_bill=models.IntegerField()
    final_bill=models.IntegerField()
    invoice=models.ImageField(upload_to="media")
    pay_mode=models.CharField(max_length=80,null=False)

class Vehicle_Management(models.Model):
    s_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    manufacturer=models.CharField(max_length=80,null=False)
    year_of_manufacturing=models.IntegerField()
    engine_no=models.CharField(max_length=40)
    chassis_no=models.CharField(max_length=40)
    colour=models.CharField(max_length=40)
    seat_capacity=models.IntegerField()
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    fuel_type=models.CharField(max_length=80,null=False)
    varient=models.CharField(max_length=80,null=False)
    km_running=models.IntegerField()
    insurance=models.ImageField(upload_to="media")
    rc_card=models.ImageField(upload_to="media")
    fitness=models.ImageField(upload_to="media")
    permit=models.ImageField(upload_to="media")
    puc=models.ImageField(upload_to="media")
    date_of_attachment=models.DateField(auto_now_add=True)
    city=models.CharField(max_length=80,null=False)
    status=models.CharField(max_length=80,null=False)


class Co_partnner_Management(models.Model):
    s_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    selfie=models.ImageField(upload_to="media")
    ower_name=models.CharField(max_length=80,null=False)
    adhar_card=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    bank_details=models.ImageField(upload_to="media")
    mobile_no=models.IntegerField()
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    payput_hourly=models.IntegerField()
    payout_daily=models.IntegerField()
    online_total_time_in_hour=models.IntegerField()
    payout=models.CharField(max_length=80,null=False)
class Country_Management(models.Model):
    s_no=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    start_date=models.CharField(max_length=80,null=False)
    office_address=models.CharField(max_length=80,null=False)
    office_contact_no=models.IntegerField()
    status=models.CharField(max_length=80,null=False)


class State_Management(models.Model):
    s_no=models.IntegerField()
    state=models.CharField(max_length=80,null=False)
    start_date=models.CharField(max_length=80,null=False)
    office_address=models.CharField(max_length=80,null=False)
    office_contact_no=models.IntegerField()
    status=models.CharField(max_length=80,null=False)


class City_Management(models.Model):
    s_no=models.IntegerField()
    city=models.CharField(max_length=80,null=False)
    start_date=models.CharField(max_length=80,null=False)
    office_address=models.CharField(max_length=80,null=False)
    office_contact_no=models.IntegerField()
    status=models.CharField(max_length=80,null=False)
class Advertisement_Management(models.Model):
    s_no=models.IntegerField()
    Promo_code_name=models.CharField(max_length=80,null=False)
    promo_code=models.CharField(max_length=80,null=False)
    vehicle_segment=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    valid_from=models.DateField(auto_now_add=True)
    valid_upto=models.DateField(auto_now_add=True)
    status_code=models.CharField(max_length=80,null=False)
    discount_type=models.IntegerField()
    user_type=models.CharField(max_length=80,null=False)
    discount_value=models.IntegerField()


class Listing_Management(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minibook_8_hrs=models.IntegerField()
    edit_button=models.CharField(max_length=80,null=False)
    image=models.ImageField(upload_to="media")
    fuel=models.ImageField(upload_to="media")
    transmission=models.CharField(max_length=80,null=False)
    seat=models.IntegerField()
    luggage=models.IntegerField()
    listing=models.CharField(max_length=80,null=False)
class City(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minibook_8_hrs=models.IntegerField()
    edit_button=models.CharField(max_length=80,null=False)
    image=models.ImageField(upload_to="media")
    fuel=models.ImageField(upload_to="media")
    transmission=models.CharField(max_length=80,null=False)
    seat=models.IntegerField()
    luggage=models.IntegerField()
    listing=models.CharField(max_length=80,null=False)
    



class RENTAL(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minibook_8_hrs=models.IntegerField()
    edit_button=models.CharField(max_length=80,null=False)
    image=models.ImageField(upload_to="media")
    fuel=models.ImageField(upload_to="media")
    transmission=models.CharField(max_length=80,null=False)
    seat=models.IntegerField()
    luggage=models.IntegerField()
    listing=models.CharField(max_length=80,null=False)
class OUTSTATATION_Second(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minibook_8_hrs=models.IntegerField()
    edit_button=models.CharField(max_length=80,null=False)
    image=models.ImageField(upload_to="media")
    fuel=models.ImageField(upload_to="media")
    transmission=models.CharField(max_length=80,null=False)
    seat=models.IntegerField()
    luggage=models.IntegerField()
    listing=models.CharField(max_length=80,null=False)
class Templates_Management(models.Model):
    s_no=models.IntegerField()
    booking_confirmation_sms=models.CharField(max_length=80,null=False)
    for_verification_otp_sms=models.CharField(max_length=80,null=False)
    resetpassword_otp=models.CharField(max_length=80,null=False)
    booking_cancel_sms=models.CharField(max_length=80,null=False)
    email_image=models.ImageField(upload_to="media")
    
        
class Fare_Management(models.Model):
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    minimum_bill=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
class City1(models.Model):
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    minimum_bill=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    


class OUTSTATATION(models.Model):
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    minimum_bill=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)


class Notification_To_Driver(models.Model):
    pass


class Notification_To_Customer(models.Model):
    pass


class Fuel_Management(models.Model):
    total_cunsumption_inr=models.IntegerField()
    diesel_cunsumption=models.IntegerField()
    petrol_cunsumption=models.IntegerField()
    cnc_cunsumption=models.IntegerField()
    cng_cunsumption=models.IntegerField()
    lpg_cunsumption=models.IntegerField()
    electricity=models.IntegerField()


class Maintainance_Management(models.Model):
    s_no=models.IntegerField()
    vehicle_no=models.CharField(max_length=80,null=False)
    date_of_services=models.DateField(auto_now_add=True)
    next_due_date_of_services=models.DateField(auto_now_add=True)
    Running_in_km=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=80,null=False)
    tyre_replace=models.DateField(auto_now_add=True)
    spare_part_invoice=models.ImageField(upload_to="media")
    insurance_claim=models.ImageField(upload_to="media")

class Refral_Management(models.Model):
    refral_content=models.CharField(max_length=80,null=False)
    refral_amount=models.IntegerField()
    refral_code=models.CharField(max_length=80,null=False)
    expiry_date=models.DateField(auto_now_add=True)
    start_date=models.DateField(auto_now_add=True)
    refral_image=models.IntegerField()
    no_user_used_code=models.IntegerField()

class Transaction_Management(models.Model):
    s_no=models.IntegerField()
    booking_id=models.CharField(max_length=80,null=False)
    gst_amount=models.IntegerField()
    gateway_charges_amount=models.IntegerField()
    amount=models.IntegerField()
    discount=models.IntegerField()
    delivery_charges=models.IntegerField()
    penalty_or_fine=models.IntegerField()
    total_amount=models.IntegerField()
    date_of_payment=models.IntegerField()
    transaction_type=models.CharField(max_length=80,null=False)
    transaction_id=models.IntegerField()
    booking_status=models.CharField(max_length=80,null=False)

class Drive_Management(models.Model):
    driver_id=models.CharField(max_length=80,null=False)
    vehicle_no=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    dl=models.ImageField(upload_to="media")
    selfie=models.ImageField(upload_to="media")
    aadhar=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    electric_bill=models.ImageField(upload_to="media")
    role=models.CharField(max_length=80,null=False)
    mobile_no=models.IntegerField()
    dl_expiry_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=80,null=False)
    shift=models.CharField(max_length=80,null=False)
    police_verfication=models.ImageField(upload_to="media")
    driver_app_login=models.EmailField(max_length=254,unique=True,null=False)
    password=models.CharField(max_length=80,null=False)
    forgot_password=models.CharField(max_length=80,null=False)




class SOS(models.Model):
    pass


class Support(models.Model):
    pass


class List_your_vehicles_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=False)
    s_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    manufacturer=models.CharField(max_length=80,null=False)
    year_of_manufacturing=models.DateField(auto_now_add=True)
    engine_no_tracing=models.ImageField(upload_to="media")
    chassis_no_tracing=models.ImageField(upload_to="media")
    colour=models.CharField(max_length=80,null=False)
    seat_capacity=models.IntegerField()
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    fuel_type=models.CharField(max_length=80,null=False)
    varient=models.CharField(max_length=80,null=False)
    km_running=models.IntegerField()
    insurance=models.ImageField(upload_to="media")
    rc_card=models.ImageField(upload_to="media")
    fitness=models.ImageField(upload_to="media")
    permit=models.ImageField(upload_to="media")
    puc=models.ImageField(upload_to="media")
    date_of_inspection=models.DateField(auto_now_add=True)
    proposed_price_day=models.DateTimeField(auto_now_add=True)
    proposed_price_night=models.DateTimeField(auto_now_add=True)
    intrested_in_attachment_after_inspection=models.BooleanField(default=False)
    city=models.CharField(max_length=80,null=False)
    selfie=models.ImageField(upload_to="media")
    Ower_name=models.CharField(max_length=80,null=False)
    aadhar_card=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    bank_details=models.ImageField(upload_to="media")
    mobile_no=models.IntegerField()
    mail_id=models.EmailField(max_length=254,unique=True,null=False)
    payout_hourly=models.IntegerField()
    payout_daily=models.IntegerField()


class Terms_Condition(models.Model):
    pass


class Privacy_Policy(models.Model):
    pass

