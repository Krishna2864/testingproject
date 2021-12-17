# Generated by Django 3.2.9 on 2021-12-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('mobile_no', models.IntegerField()),
                ('option', models.CharField(max_length=80)),
                ('listview', models.CharField(max_length=80)),
                ('set_permission', models.BooleanField(default=False)),
                ('set_permission_co_partner', models.BooleanField(default=False)),
                ('set_permission_country', models.BooleanField(default=False)),
                ('set_permission_state', models.BooleanField(default=False)),
                ('set_permission_advertisement', models.BooleanField(default=False)),
                ('set_permission_listing', models.BooleanField(default=False)),
                ('set_permission_templates', models.BooleanField(default=False)),
                ('set_permission_fare', models.BooleanField(default=False)),
                ('set_permission_notification', models.BooleanField(default=False)),
                ('set_permission_notification2', models.BooleanField(default=False)),
                ('set_permission_fuel', models.BooleanField(default=False)),
                ('set_permission_maintainance', models.BooleanField(default=False)),
                ('set_permission_refral', models.BooleanField(default=False)),
                ('set_permission_refund', models.BooleanField(default=False)),
                ('set_permission_trasaction', models.BooleanField(default=False)),
                ('set_permission_feedback', models.BooleanField(default=False)),
                ('set_permission_sos', models.BooleanField(default=False)),
                ('set_permission_support', models.BooleanField(default=False)),
                ('set_permission_other', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('Promo_code_name', models.CharField(max_length=80)),
                ('promo_code', models.CharField(max_length=80)),
                ('vehicle_segment', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('valid_from', models.DateField(auto_now_add=True)),
                ('valid_upto', models.DateField(auto_now_add=True)),
                ('status_code', models.CharField(max_length=80)),
                ('discount_type', models.IntegerField()),
                ('user_type', models.CharField(max_length=80)),
                ('discount_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('city', models.CharField(max_length=80)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('office_address', models.CharField(max_length=180)),
                ('office_contact_no', models.IntegerField()),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Co_partnner_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('vehicle_registration_no', models.CharField(max_length=80)),
                ('selfie', models.ImageField(upload_to='media')),
                ('ower_name', models.CharField(max_length=80)),
                ('adhar_card', models.ImageField(upload_to='media')),
                ('pan_card', models.ImageField(upload_to='media')),
                ('bank_details', models.ImageField(upload_to='media')),
                ('mobile_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('payput_hourly', models.IntegerField()),
                ('payout_daily', models.IntegerField()),
                ('online_total_time_in_hour', models.IntegerField()),
                ('payout', models.CharField(max_length=80)),
                ('history', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Country_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('office_address', models.CharField(max_length=180)),
                ('office_contact_no', models.IntegerField()),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Fare_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('segment', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('price_hour_400KM', models.IntegerField()),
                ('price_day_400', models.IntegerField()),
                ('price_hour_or_ul_km', models.IntegerField()),
                ('price_day_or_ul_km', models.IntegerField()),
                ('gst', models.IntegerField()),
                ('gateway', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cunsumption_inr', models.IntegerField()),
                ('diesel_cunsumption', models.IntegerField()),
                ('petrol_cunsumption', models.IntegerField()),
                ('cnc_cunsumption', models.IntegerField()),
                ('cng_cunsumption', models.IntegerField()),
                ('lpg_cunsumption', models.IntegerField()),
                ('electricity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='List_your_vehicles_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=80)),
                ('s_no', models.IntegerField()),
                ('vehicle_registration_no', models.CharField(max_length=80)),
                ('manufacturer', models.CharField(max_length=80)),
                ('year_of_manufacturing', models.DateField(auto_now_add=True)),
                ('engine_no_tracing', models.ImageField(upload_to='media')),
                ('chassis_no_tracing', models.ImageField(upload_to='media')),
                ('colour', models.CharField(max_length=80)),
                ('seat_capacity', models.IntegerField()),
                ('segment', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('fuel_type', models.CharField(max_length=80)),
                ('varient', models.CharField(max_length=80)),
                ('km_running', models.IntegerField()),
                ('insurance', models.ImageField(upload_to='media')),
                ('rc_card', models.ImageField(upload_to='media')),
                ('fitness', models.ImageField(upload_to='media')),
                ('permit', models.ImageField(upload_to='media')),
                ('puc', models.ImageField(upload_to='media')),
                ('date_of_inspection', models.DateField(auto_now_add=True)),
                ('proposed_price_day', models.DateTimeField(auto_now_add=True)),
                ('proposed_price_night', models.DateTimeField(auto_now_add=True)),
                ('intrested_in_attachment_after_inspection', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=80)),
                ('selfie', models.ImageField(upload_to='media')),
                ('Ower_name', models.CharField(max_length=80)),
                ('aadhar_card', models.ImageField(upload_to='media')),
                ('pan_card', models.ImageField(upload_to='media')),
                ('bank_details', models.ImageField(upload_to='media')),
                ('mobile_no', models.IntegerField()),
                ('mail_id', models.EmailField(max_length=254, unique=True)),
                ('payout_hourly', models.IntegerField()),
                ('payout_daily', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('vehicle_id', models.CharField(max_length=80)),
                ('segment', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('price_hour_400KM', models.IntegerField()),
                ('price_day_400', models.IntegerField()),
                ('price_hour_or_ul_km', models.IntegerField()),
                ('price_day_or_ul_km', models.IntegerField()),
                ('gst', models.IntegerField()),
                ('gateway', models.IntegerField()),
                ('available_after_completion_of_2hr_of_existing_trip', models.CharField(max_length=80)),
                ('minibook_8_hrs', models.CharField(max_length=80)),
                ('edit_button', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='media')),
                ('fuel', models.CharField(max_length=80)),
                ('transmission', models.CharField(max_length=80)),
                ('seat', models.IntegerField()),
                ('luggage', models.IntegerField()),
                ('listing', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Maintainance_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('vehicle_no', models.CharField(max_length=80)),
                ('date_of_services', models.DateField(auto_now_add=True)),
                ('next_due_date_of_services', models.DateField(auto_now_add=True)),
                ('Running_km', models.IntegerField()),
                ('status', models.CharField(max_length=80)),
                ('tyre_replace', models.DateField(auto_now_add=True)),
                ('spare_part_invoice', models.ImageField(upload_to='media')),
                ('insurance_claim', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Notification_To_CoPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Notification_To_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_doc_submission', models.CharField(max_length=150)),
                ('under_verification', models.CharField(max_length=150)),
                ('verified', models.CharField(max_length=150)),
                ('reverify', models.CharField(max_length=150)),
                ('sorry', models.CharField(max_length=150)),
                ('booking_confirmed', models.CharField(max_length=150)),
                ('before_book_start', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Refral_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refral_content', models.CharField(max_length=200)),
                ('refral_amount', models.IntegerField()),
                ('refral_code', models.CharField(max_length=80)),
                ('Expiry_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('refral_image', models.ImageField(upload_to='media')),
                ('no_user_used_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Refund_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('booking_id', models.CharField(max_length=80)),
                ('gst_amount', models.IntegerField()),
                ('gateway_charges_amount', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('cancellation_charges', models.IntegerField()),
                ('booking_amount', models.IntegerField()),
                ('total_refund_amount', models.IntegerField()),
                ('date_of_refounded', models.DateField(auto_now_add=True)),
                ('model', models.CharField(max_length=80)),
                ('transaction_id', models.IntegerField()),
                ('booking_status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='SOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='state_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('state', models.CharField(max_length=80)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('office_address', models.CharField(max_length=180)),
                ('office_contact_no', models.IntegerField()),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Templates_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('booking_confirmation_sms', models.CharField(max_length=100)),
                ('for_verification_otp_sms', models.CharField(max_length=80)),
                ('resetpassword_otp', models.CharField(max_length=80)),
                ('booking_cancel_sms', models.CharField(max_length=80)),
                ('email_image', models.ImageField(upload_to='media')),
                ('email_invoice', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Terms_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('booking_id', models.CharField(max_length=80)),
                ('gst_amount', models.IntegerField()),
                ('gateway_charges_amount', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('delivery_charges', models.IntegerField()),
                ('penalty_or_fine', models.IntegerField()),
                ('date_of_payment', models.DateField(auto_now_add=True)),
                ('transaction_type', models.CharField(max_length=80)),
                ('transaction_id', models.IntegerField()),
                ('booking_status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='User_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_user', models.CharField(max_length=40)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.IntegerField()),
                ('pan_card', models.ImageField(upload_to='media')),
                ('selfie', models.ImageField(upload_to='media')),
                ('full_name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=40)),
                ('blood_group', models.CharField(max_length=80)),
                ('emergency_contact_no', models.IntegerField()),
                ('driving_license_no', models.ImageField(upload_to='media')),
                ('aadhar_card_or_passport_front', models.ImageField(upload_to='media')),
                ('adhar_card_or_passport_back', models.ImageField(upload_to='media')),
                ('expiry_of_driving_license', models.DateField(auto_now_add=True)),
                ('occupation', models.CharField(max_length=80)),
                ('father_name', models.CharField(max_length=80)),
                ('mother_name', models.CharField(max_length=80)),
                ('permanent_address', models.CharField(max_length=180)),
                ('local_address', models.CharField(max_length=180)),
                ('local_three_landmark', models.CharField(max_length=80)),
                ('vehicle_requirement', models.CharField(max_length=80)),
                ('purpose_of_vehicle_requirement', models.CharField(max_length=40)),
                ('vehicle_pickup_time', models.DateTimeField(auto_now_add=True)),
                ('vehicle_drop_time', models.DateTimeField(auto_now_add=True)),
                ('fuel_level', models.CharField(max_length=80)),
                ('alloted_vehicle', models.CharField(max_length=80)),
                ('refund', models.IntegerField()),
                ('verify_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=80)),
                ('s_no', models.IntegerField()),
                ('vehicle_registration_no', models.CharField(max_length=80)),
                ('manufacturer', models.CharField(max_length=80)),
                ('year_of_manufacturing', models.IntegerField()),
                ('engine_no', models.CharField(max_length=40)),
                ('chassis_no', models.CharField(max_length=40)),
                ('colour', models.CharField(max_length=40)),
                ('seat_capacity', models.IntegerField()),
                ('segment', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('fuel_type', models.CharField(max_length=80)),
                ('varient', models.CharField(max_length=80)),
                ('km_running', models.IntegerField()),
                ('insurance', models.ImageField(upload_to='media')),
                ('rc_card', models.ImageField(upload_to='media')),
                ('fitness', models.ImageField(upload_to='media')),
                ('permit', models.ImageField(upload_to='media')),
                ('puc', models.ImageField(upload_to='media')),
                ('date_of_attachment', models.DateField(auto_now_add=True)),
                ('city', models.CharField(max_length=80)),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_vehicle', models.IntegerField()),
                ('running_vehicle', models.IntegerField()),
                ('breakdown_vehicle', models.IntegerField()),
                ('maintainance_vehicle', models.IntegerField()),
                ('free_vehicle', models.IntegerField()),
                ('map_view', models.CharField(max_length=80)),
                ('vehicle_no', models.CharField(max_length=80)),
                ('view', models.CharField(max_length=80)),
                ('mobile_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
