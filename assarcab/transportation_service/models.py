from django.db import models

# Create your models here.
class Vehicle_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=False)
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


class Driver_Mangement(models.Model):
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

class Copartner_Management(models.Model):
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


class Refral_mangemnt(models.Model):
    refral_content=models.CharField(max_length=200)
    refral_amount=models.IntegerField()
    refral_code=models.CharField(max_length=80,null=False)
    Expiry_date=models.DateField(auto_now_add=True)
    start_date=models.DateField(auto_now_add=True)
    refral_image=models.ImageField(upload_to="media")
    no_user_used_code=models.IntegerField()



class Notification_to_Driver(models.Model):
    pass


class Fuel_Mangement(models.Model):
    total_cunsumption_inr=models.IntegerField()
    diesel_cunsumption=models.IntegerField()
    petrol_cunsumption=models.IntegerField()
    cnc_cunsumption=models.IntegerField()
    cng_cunsumption=models.IntegerField()
    lpg_cunsumption=models.IntegerField()
    electricity=models.IntegerField()


class Maintenance_Management(models.Model):
    s_no=models.IntegerField()
    vehicle_no=models.CharField(max_length=80,null=False)
    date_of_services=models.DateField(auto_now_add=True)
    next_due_date_of_services=models.DateField(auto_now_add=True)
    Running_km=models.IntegerField()
    status=models.CharField(max_length=80,null=False)
    tyre_replace=models.DateField(auto_now_add=True)
    spare_part_invoice=models.ImageField(upload_to="media")
    insurance_claim=models.ImageField(upload_to="media")




class fARE_MGMT(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    fuel_status=models.CharField(max_length=80,null=False)
    trip_type=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minimum_bill=models.IntegerField()    
    toll_tax=models.IntegerField()   
    parking=models.IntegerField()
    seat=models.IntegerField()



class Listing_Management(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    fuel_status=models.CharField(max_length=80,null=False)
    trip_type=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minimum_bill=models.IntegerField()    
    toll_tax=models.IntegerField()    
    seat=models.IntegerField()
    image=models.ImageField(upload_to="media")
    edit_button=models.CharField(max_length=80,null=False)
    listing=models.CharField(max_length=80,null=False)
    


class OUTSTATION(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    fuel_status=models.CharField(max_length=80,null=False)
    trip_type=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minimum_bill=models.IntegerField()    
    toll_tax=models.IntegerField()    
    seat=models.IntegerField()
    image=models.ImageField(upload_to="media")
    edit_button=models.CharField(max_length=80,null=False)
    listing=models.CharField(max_length=80,null=False)
    


class Transaction_Management(models.Model):
    booking_id=models.IntegerField()
    gst=models.FloatField()
    gateway_charges_amount=models.IntegerField()
    discount=models.IntegerField()
    segment=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    gst=models.IntegerField()
    insurance=models.IntegerField()
    extra_km=models.IntegerField()
    waitng_charge=models.IntegerField()
    night_charge=models.IntegerField()
    driver_charge=models.IntegerField()
    discount=models.IntegerField()
    minimum_bill=models.IntegerField()
    final_bill=models.IntegerField()
    invoice=models.ImageField(upload_to="media")
    pay_mode=models.IntegerField()  




class LIST_YOUR_VEHICLE_MGMT(models.Model):
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
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    payout_hourly=models.IntegerField()
    payout_daily=models.IntegerField()



class Feedback(models.Model):
    pass


class TERMS_CONDITIONS(models.Model):
    pass


class PRIVACY_POLICY(models.Model):
    pass

