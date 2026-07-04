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