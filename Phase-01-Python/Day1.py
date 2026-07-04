#****************************VARIABLES***************************
# Hospital Management System - Basic Example using Variables

# Hospital details
hospital_name = "City Care Hospital" # Hospital ka name bata raha h ye variable
hospital_address = "123 Main Street, Karachi" # ye hospital ka address bata raha h 
total_beds = 200 # hospital  main total kitny beds hyn 
available_beds = 45 # is waqt kitny beds avaliable hyn 

# Patient details
costumer_name = "Ahmed Khan" # paietnt ka naame
patient_id = "P-10234" #patient ki Identification no
patient_age = 34 #Pateint ki age 
patient_gender = "Male" #Uska gender 
patient_blood_group = "O+" #Patinet ka blood group
is_admitted = True # Paitent hospital main admit h ya nhi ye bata raha h 
room_number = "B-204"# Konsy room main h
admission_date = "2026-07-01" # Admit kab hoa h 

# Doctor details
consultant_name = "Dr. Sara Ali" #Doctor ka naam
doctor_specialization = "Cardiologist" #Dr ki speciality
doctor_experience_years = 12 # Dr ka experiance
consultation_fee = 1500  # in PKR #Dr ki checkup fee

# Billing details
room_charges_per_day = 3000 #Per day room k charges
medicine_charges = 2500 # Medicins charges
lab_test_charges = 4000 # lab test charges
days_admitted = 5 # Kitny days se admit h 
'''
Task 3
Khud mujhe jawab dena:
Variable aur value mein difference kya hai?
variables bataty hyn k usmain konsa data store h kia store h aur value wo stored data hoti h 
Agar variable na hote to programming kitni mushkil hoti?
agar variables na hoty to data store nhi hpata agar data nhi hota to AI bhi nhi hoti
AI Engineer ko variable ka concept deeply kyun samajhna chahiye?
taky wo achi tarah data ko smjh kr ek achy AI Product develop krsky
'''

#*****************************DATA TYPES***********************
#Task 01
# Hospital Patient Record - Using Major Python Data Types

# 1. int - Whole numbers (kiun k AGe, room number aur Patient id whole number hoty hyn isliye int type use ki)
patient_id = 10234
age = 34
room_number = 204

# 2. float - Decimal numbers (body temp, weight, height decimal mian bhi hosktin hyn is liye int k bajaye float use kiya)
body_temperature = 98.6
weight_kg = 72.5
height_m = 1.75

# 3. str - Text/String (name, blood group, gender inmain kabhi bi koi number nhi sirf simple text aata  h isliye string type use ki )
patient_name = "Ahmed Khan"
blood_group = "O+"
gender = "Male"

# 4. bool - True/False  (admit hoga ya nhi aur isi tarah insured hoga ya nhi ye 2 hi possible values hosktin yn aur jahan sir yes ya No ka use ho wahan hm boolen data tyep ka use krty hyn )
is_admitted = True
is_insured = False

# 5. NoneType - Represents "no value yet" (e.g., discharge date not set)
discharge_date = None

# 6. list - Ordered, mutable collection (e.g., symptoms reported)
symptoms = ["fever", "cough", "fatigue"]

# 7. tuple - (patient ko jb admit karaya tha us waqt ko vitals thy wo dobara nhi hoskty isi liye jo cheez immutable ho usko hm tup;e main store krty hyn is lliye tuple use koya )
admission_vitals = (98.6, 120, 80)  # (temperature, systolic BP, diastolic BP)

# 8. set - (allergies ek se ziyada hosktin hyn aur ek jesi 2 nhi hosktin is liye set type ka use kiya k jahan data unordered ho sath main usmain repetation na ho duplicate value na ho )
allergies = {"penicillin", "dust", "peanuts"}

# 9. dict - Key-value pairs (e.g., full patient record combining everything)
patient_record = {
    "id": patient_id,
    "name": patient_name,
    "age": age,
    "gender": gender,
    "blood_group": blood_group,
    "weight_kg": weight_kg,
    "height_m": height_m,
    "is_admitted": is_admitted,
    "is_insured": is_insured,
    "discharge_date": discharge_date,
    "symptoms": symptoms,
    "admission_vitals": admission_vitals,
    "allergies": allergies,
}

#Task 02
'''
Ye code dekho:
patient = {
    "name": "Ahmed",
    "age": 45,
    "weight": 82.5,
    "is_diabetic": False,
    "allergies": ["Penicillin", "Dust"],
    "doctor": None
}
Mujhe batana:
patient ka data type?
"name" ki value ka data type?
"age"?
"weight"?
"is_diabetic"?
"allergies"?
"doctor"?
Aur sabse important:
doctor = None kyun rakha gaya? Empty string "" kyun nahi?
'''
patient = {
    "name": "Ahmed", #String
    "age": 45, #Int
    "weight": 82.5, #float
    "is_diabetic": False, #Boolean
    "allergies": ["Penicillin", "Dust"], #List
    "doctor": None #None
}
#doctor = None kyun rakha gaya? Empty string "" kyun nahi?
#Iska answer nhi pata 


#Task 03:
'''
Suppose tum AI Hospital bana rahe ho.
Neeche diye gaye data ko sahi Data Type assign karo aur kyun bhi likho:
Patient Name  String because simple text
Patient Age Int because whole number
Blood Group string beacuse simple text
Height float beacuse decimal main bhi value hoskti h 
Weight   float beacuse decimal main bhi value hoskti h
Is Pregnant?   Boolean beacuse ya to pregnant hoga ya nhi 
Medicines List  List beacuse ek se ziayad medicein hoskitn yn 
Emergency Contact   Int aur string donon main hoskta h 
GPS Location  Tuple beacuse location imuutable h
Previous Diseases  Tuple kiun k pechla data change nhi hota
Next Appointment (abhi schedule nahi hui) None kiun k abhi koi value assign nhi hoi 
'''

#***************Operators************************
#Task 1:
# Hospital Billing System - Demonstrating All Major Python Operators

# ---------------------------------------------------
# Patient & Charges Data
# ---------------------------------------------------
patient_name = "Ahmed Khan"
is_insured = True
is_senior_citizen = True
days_admitted = 5
room_charges_per_day = 3000
medicine_charges = 2500
lab_test_charges = 4000
consultation_fee = 1500
insurance_coverage_percent = 40
senior_discount_percent = 10

# ---------------------------------------------------
# 1. ARITHMETIC OPERATORS ( + - * / // % ** )
# ---------------------------------------------------
total_room_charges = room_charges_per_day * days_admitted          # multiplication (yhn pr total room k charges nnikalny k liye multiply ka use kia k per day room k kia chargs hyn aur kitny din se admit h to us waqt se lykr current day tk k total bill kitna hoa)
subtotal = total_room_charges + medicine_charges + lab_test_charges + consultation_fee  # addition  (sari fees milakr total bill kitna hoa is liye use kia gaya h )
average_daily_cost = subtotal / days_admitted                      # division (float)  (daily cost ka average niaklny k liye )
full_days = subtotal // 1000                                       # floor division
remainder_amount = subtotal % 1000                                 # modulus (remainder amount wapas kitny krny hyn usko chezk krny k liye modules lagaya )
loyalty_bonus = 2 ** 3                                              # exponent (sample bonus points)

# ---------------------------------------------------
# 2. ASSIGNMENT OPERATORS ( = += -= *= /= )
# ---------------------------------------------------
final_bill = subtotal   # simple assignment (= ka use finall bill main subtotal ki value assign krny k liye hoa )

if is_insured:
    discount_amount = final_bill * (insurance_coverage_percent / 100)
    final_bill -= discount_amount     # -= operator final bill i amount se discounted amount ko minus krny k liye lagaya

if is_senior_citizen:
    senior_discount = final_bill * (senior_discount_percent / 100)
    final_bill -= senior_discount     # -= operator final bill amount main se senior citizen ka jo discounted amount h wo niaklny k lliye lagaya

late_fee = 500
final_bill += late_fee                # += operator final bill main late fee include krny k liye lagaya

# ---------------------------------------------------
# 3. COMPARISON OPERATORS ( == != > < >= <= )
# ---------------------------------------------------
is_bill_high = final_bill > 10000 #> ka use is liye hoa taky ye chekc kiya ja sky k final bill ki amount 100000 se ziyada h ya nhi 
is_bill_low = final_bill < 5000 #< ka use is liye hoa taky ye chekc kiya ja sky k final bill ki amount 100000 se kam h ya nhi
is_exact_5_days = days_admitted == 5 # == ka use exact 5 days hyn ya nhi ye check krny k liye hoa 
not_insured = is_insured != True #!= ka use ye krny k  liye hoa k insured h ya nhi 
# ---------------------------------------------------
# 4. LOGICAL OPERATORS ( and or not )
# ---------------------------------------------------
eligible_for_extra_discount = is_insured and is_senior_citizen        # and is liye use kiya taky check kiya jaye k patent insured aur senior citizen h yanhi 
needs_review = is_bill_high or not is_insured                         # or / not  patietn ko review ki need h agar uska bill high ya wo insured nhi hao to in main se ek bhi conidtion true hogi to usko review ki need hogi other wise no 
priority_case = not is_insured                                        # not ka use priority check krny k liye hoa k agar insured nhi  h patient to priority den gy otherwise no 

# ---------------------------------------------------
# 5. IDENTITY OPERATORS ( is / is not )
# ---------------------------------------------------
discharge_date = None 
is_discharge_pending = discharge_date is None # is ka use es liye hoa k chekc kiya jae k discharge date asign hoi h ya nhi 
payment_status = "Paid"
is_not_pending = payment_status is not None # i not ka use es liye hoa taky check kiya  jaye k payment status paid to nhi hoa 
# ---------------------------------------------------
# 6. MEMBERSHIP OPERATORS ( in / not in )
# ---------------------------------------------------
available_departments = ["Cardiology", "Neurology", "Orthopedics", "General"]
patient_department = "Cardiology"
is_valid_department = patient_department in available_departments # in ka use is liye hoa taky check kiya jae k availiable dept main patient dept h ya nhi 
is_invalid_service = "Dental" not in available_departments

'''
Task 2
Is code ko dekho:
patient_age = 65
sugar_level = 210
allergies = ["Penicillin", "Dust"]
doctor = None

is_high_risk = patient_age > 60 and sugar_level > 180

if "Penicillin" in allergies:
    print("Alert")

if doctor is None:
    print("Assign Doctor")

Batana:
> kis type ka operator hai?
and?
in?
is?
=?
Aur har operator yahan kyun use hua?
'''
patient_age = 65
sugar_level = 210
allergies = ["Penicillin", "Dust"]
doctor = None

is_high_risk = patient_age > 60 and sugar_level > 180

if "Penicillin" in allergies:
    print("Alert")

if doctor is None:
    print("Assign Doctor")

# > comparision operator h aur ye is liye use hoa taky check kiya jaye k patient age 60 se above h ya  nhi aur and logical operator h iska use is liye hoa taky check kiya jaye k patietn age 60 se aur suger level 180 se above h ya nhi matlab ye doonon cheezyn hyn ya nhi agar hyn to usko store krdo isrosk high nam k variabl main
# in membership operator h iska use is liye hoa taky dekha jaye k allergies main Penicillin  h ya nhi agar h to ALert print ho is identity operator h ye use hoa taky dekha jaye  doctor assgin hoa ya nhi , = assignment operaotr h iska use is liye hoa taky patient_age > 60 and sugar_level > 180 ko is_high_risk main  store kiya jaye

'''
Task 3 (Engineer Thinking)
Suppose tum AI Hospital bana rahe ho.
Neeche diye gaye scenarios mein kaunsa operator use hoga aur kyun?
Bill mein medicine charges add karne hain.
+ addition krny k liye yhi arithmetic operatr k use hta h 
Check karna hai patient ki age 18 se zyada hai ya nahi.
> is liye kiunk chota bara check krny k liye yhi comparisio operator ka use hota  h
Check karna hai patient diabetic aur hypertensive dono hai.
and logical operator kiun k donon cheezyn check krni hyn donon condition true hon is ky liye and operator ka use hota h 
Check karna hai "Aspirin" allergies list mein hai ya nahi.
in ye item is list ka  member h ya nhi ye dekhny k liye in membership operator ka use hotah 
Check karna hai doctor abhi assign nahi hua.
dontor ki identity check krny k liye is operator ka use hoga 
'''