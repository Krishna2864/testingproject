from django.db import models
# Create your models here.
class Admin_Management(models.Model):
    s_no=models.IntegerField(null=False)
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    name=models.CharField(max_length=80,null=False)
    username=models.CharField(max_length=80,null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    mobile_no=models.IntegerField(null=False)
    option=models.CharField(max_length=80,null=False)
    listview=models.CharField(max_length=80,null=False)
    set_permission=models.BooleanField(default=False)
    set_permission_co_partner=models.BooleanField(default=False)
    set_permission_country=models.BooleanField(default=False)
    set_permission_state=models.BooleanField(default=False)
    set_permission_advertisement=models.BooleanField(default=False)
    set_permission_listing=models.BooleanField(default=False)
    set_permission_templates=models.BooleanField(default=False)
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
    new_user=models.CharField(max_length=40)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    contact_no=models.IntegerField(null=False)
    pan_card=models.ImageField(upload_to="media")
    selfie=models.ImageField(upload_to="media")
    full_name=models.CharField(max_length=80,null=False)
    age=models.IntegerField(null=False)
    gender=models.CharField(max_length=40)
    blood_group=models.CharField(max_length=80,null=False)
    emergency_contact_no=models.IntegerField(null=False)
    driving_license_no=models.ImageField(upload_to="media")
    aadhar_card_or_passport_front=models.ImageField(upload_to="media")
    adhar_card_or_passport_back=models.ImageField(upload_to="media")
    expiry_of_driving_license=models.DateField(auto_now_add=True)
    occupation=models.CharField(max_length=80,null=False)
    father_name=models.CharField(max_length=80,null=False)
    mother_name=models.CharField(max_length=80,null=False)
    permanent_address=models.CharField(max_length=180)
    local_address=models.CharField(max_length=180)
    local_three_landmark=models.CharField(max_length=80,null=False)
    vehicle_requirement=models.CharField(max_length=80,null=False)
    purpose_of_vehicle_requirement=models.CharField(max_length=40)
    vehicle_pickup_time=models.DateTimeField(auto_now_add=True)
    vehicle_drop_time=models.DateTimeField(auto_now_add=True)
    fuel_level=models.CharField(max_length=80,null=False)
    alloted_vehicle=models.CharField(max_length=80,null=False)
    refund=models.IntegerField(null=False)
    verify_status=models.BooleanField(default=False)

    


class Vehicle_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=False)
    s_no=models.IntegerField(null=False)
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    manufacturer=models.CharField(max_length=80,null=False)
    year_of_manufacturing=models.IntegerField(null=False)
    engine_no=models.CharField(max_length=40)
    chassis_no=models.CharField(max_length=40)
    colour=models.CharField(max_length=40)
    seat_capacity=models.IntegerField(null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    fuel_type=models.CharField(max_length=80,null=False)
    varient=models.CharField(max_length=80,null=False)
    km_running=models.IntegerField(null=False)
    insurance=models.ImageField(upload_to="media")
    rc_card=models.ImageField(upload_to="media")
    fitness=models.ImageField(upload_to="media")
    permit=models.ImageField(upload_to="media")
    puc=models.ImageField(upload_to="media")
    date_of_attachment=models.DateField(auto_now_add=True)
    city=models.CharField(max_length=80,null=False)
    status=models.CharField(max_length=80,null=False)



class List_your_vehicles_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=False)
    s_no=models.IntegerField(null=False)
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    manufacturer=models.CharField(max_length=80,null=False)
    year_of_manufacturing=models.DateField(auto_now_add=True)
    engine_no_tracing=models.ImageField(upload_to="media")
    chassis_no_tracing=models.ImageField(upload_to="media")
    colour=models.CharField(max_length=80,null=False)
    seat_capacity=models.IntegerField(null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    fuel_type=models.CharField(max_length=80,null=False)
    varient=models.CharField(max_length=80,null=False)
    km_running=models.IntegerField(null=False)
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
    mobile_no=models.IntegerField(null=False)
    mail_id=models.EmailField(max_length=254,unique=True,null=False)
    payout_hourly=models.IntegerField(null=False)
    payout_daily=models.IntegerField(null=False)
    



class Vehicle_Monitoring(models.Model):
    total_vehicle=models.IntegerField(null=False)
    running_vehicle=models.IntegerField(null=False)
    breakdown_vehicle=models.IntegerField(null=False)
    maintainance_vehicle=models.IntegerField(null=False)
    free_vehicle=models.IntegerField(null=False)
    map_view=models.CharField(max_length=80,null=False)
    vehicle_no=models.CharField(max_length=80,null=False)
    view=models.CharField(max_length=80,null=False)
    mobile_no=models.IntegerField(null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)


class Co_partnner_Management(models.Model):
    s_no=models.IntegerField(null=False)
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    selfie=models.ImageField(upload_to="media")
    ower_name=models.CharField(max_length=80,null=False)
    adhar_card=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    bank_details=models.ImageField(upload_to="media")
    mobile_no=models.IntegerField(null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    payput_hourly=models.IntegerField(null=False)
    payout_daily=models.IntegerField(null=False)
    online_total_time_in_hour=models.IntegerField(null=False)
    payout=models.CharField(max_length=80,null=False)
    history=models.CharField(max_length=80,null=False)


class Country_Management(models.Model):
    s_no=models.IntegerField(null=False)
    country=models.CharField(max_length=80,null=False)
    start_date=models.DateField(auto_now_add=True)
    office_address=models.CharField(max_length=180)
    office_contact_no=models.IntegerField(null=False)
    status=models.CharField(max_length=80,null=False)


class state_Management(models.Model):
    s_no=models.IntegerField(null=False)
    state=models.CharField(max_length=80,null=False)
    start_date=models.DateField(auto_now_add=True)
    office_address=models.CharField(max_length=180)
    office_contact_no=models.IntegerField(null=False)
    status=models.CharField(max_length=80,null=False)

class City_Management(models.Model):
    s_no=models.IntegerField(null=False)
    city=models.CharField(max_length=80,null=False)
    start_date=models.DateField(auto_now_add=True)
    office_address=models.CharField(max_length=180)
    office_contact_no=models.IntegerField(null=False)
    status=models.CharField(max_length=80,null=False)


class Advertisement_Management(models.Model):
    s_no=models.IntegerField(null=False)
    Promo_code_name=models.CharField(max_length=80,null=False)
    promo_code=models.CharField(max_length=80,null=False)
    vehicle_segment=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    valid_from=models.DateField(auto_now_add=True)
    valid_upto=models.DateField(auto_now_add=True)
    status_code=models.CharField(max_length=80,null=False)
    discount_type=models.IntegerField(null=False)
    user_type=models.CharField(max_length=80,null=False)
    discount_value=models.IntegerField(null=False)


class Listing_Management(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    price_hour_400KM=models.IntegerField(null=False)
    price_day_400=models.IntegerField(null=False)
    price_hour_or_ul_km=models.IntegerField(null=False)
    price_day_or_ul_km=models.IntegerField(null=False)
    gst=models.IntegerField(null=False)
    gateway=models.IntegerField(null=False)
    available_after_completion_of_2hr_of_existing_trip=models.CharField(max_length=80,null=False)
    minibook_8_hrs=models.CharField(max_length=80,null=False)
    edit_button=models.CharField(max_length=80,null=False)
    image=models.ImageField(upload_to="media")  
    fuel=models.CharField(max_length=80,null=False)
    transmission=models.CharField(max_length=80,null=False)
    seat=models.IntegerField(null=False)
    luggage=models.IntegerField(null=False)
    listing=models.CharField(max_length=80,null=False)


class Templates_Management(models.Model):
    s_no=models.IntegerField(null=False)
    booking_confirmation_sms=models.CharField(max_length=100)
    for_verification_otp_sms=models.CharField(max_length=80,null=False)
    resetpassword_otp=models.CharField(max_length=80,null=False)
    booking_cancel_sms=models.CharField(max_length=80,null=False)
    email_image=models.ImageField(upload_to="media")
    email_invoice=models.CharField(max_length=80,null=False)


class Fare_Management(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    price_hour_400KM=models.IntegerField(null=False)
    price_day_400=models.IntegerField(null=False)
    price_hour_or_ul_km=models.IntegerField(null=False)
    price_day_or_ul_km=models.IntegerField(null=False)
    gst=models.IntegerField(null=False)
    gateway=models.IntegerField(null=False)
class Notification_To_User(models.Model):
    for_doc_submission=models.CharField(max_length=150)
    under_verification=models.CharField(max_length=150)
    verified=models.CharField(max_length=150)
    reverify=models.CharField(max_length=150)
    sorry=models.CharField(max_length=150)
    booking_confirmed=models.CharField(max_length=150)
    before_book_start=models.CharField(max_length=150)


class Notification_To_CoPartner(models.Model):
    pass


class Fuel_Management(models.Model):
    total_cunsumption_inr=models.IntegerField(null=False)
    diesel_cunsumption=models.IntegerField(null=False)
    petrol_cunsumption=models.IntegerField(null=False)
    cnc_cunsumption=models.IntegerField(null=False)
    cng_cunsumption=models.IntegerField(null=False)
    lpg_cunsumption=models.IntegerField(null=False)
    electricity=models.IntegerField(null=False)



class Maintainance_Management(models.Model):
    s_no=models.IntegerField(null=False)
    vehicle_no=models.CharField(max_length=80,null=False)
    date_of_services=models.DateField(auto_now_add=True)
    next_due_date_of_services=models.DateField(auto_now_add=True)
    Running_km=models.IntegerField(null=False)
    status=models.CharField(max_length=80,null=False)
    tyre_replace=models.DateField(auto_now_add=True)
    spare_part_invoice=models.ImageField(upload_to="media")
    insurance_claim=models.ImageField(upload_to="media")



class Refral_Management(models.Model):
    refral_content=models.CharField(max_length=200)
    refral_amount=models.IntegerField(null=False)
    refral_code=models.CharField(max_length=80,null=False)
    Expiry_date=models.DateField(auto_now_add=True)
    start_date=models.DateField(auto_now_add=True)
    refral_image=models.ImageField(upload_to="media")
    no_user_used_code=models.IntegerField(null=False)



class Refund_Management(models.Model):
    s_no=models.IntegerField(null=False)
    booking_id=models.CharField(max_length=80,null=False)
    gst_amount=models.IntegerField(null=False)
    gateway_charges_amount=models.IntegerField(null=False)
    amount=models.IntegerField(null=False)
    cancellation_charges=models.IntegerField(null=False)
    booking_amount=models.IntegerField(null=False)
    total_refund_amount=models.IntegerField(null=False)
    date_of_refounded=models.DateField(auto_now_add=True)
    model=models.CharField(max_length=80,null=False)
    transaction_id=models.IntegerField(null=False)
    booking_status=models.CharField(max_length=80,null=False)


class Transaction_Management(models.Model):
    s_no=models.IntegerField(null=False)
    booking_id=models.CharField(max_length=80,null=False)
    gst_amount = models.IntegerField(null=False)
    gateway_charges_amount=models.IntegerField(null=False)
    amount=models.IntegerField(null=False)
    discount=models.IntegerField(null=False)
    delivery_charges=models.IntegerField(null=False)
    penalty_or_fine=models.IntegerField(null=False)
    total_amount=models.IntegerField
    date_of_payment=models.DateField(auto_now_add=True)
    transaction_type=models.CharField(max_length=80,null=False)
    transaction_id=models.IntegerField(null=False)
    booking_status=models.CharField(max_length=80,null=False)

class Feedback(models.Model):
    pass


class Content_Management(models.Model):
    pass


class SOS(models.Model):
    pass


class Support(models.Model):
    pass


class Terms_Condition(models.Model):
    pass


class Privacy_Policy(models.Model):
    pass

