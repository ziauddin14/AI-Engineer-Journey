"""
Hospital Management System - List, Tuple, Set & Dictionary Demo
Author: Zia's AI Engineer Journey - Phase 01 (Python)
"""
# LIST -> Ordered, changeable collection
# Used here for: Patient queue (order matters, can add/remove)
#If we use tuple so we can't change patients, if use set so we can't insert duplicate names of patients, and we can't use dict also bcz here is no key value pair available
patient_queue = ["Ali", "Sara", "Ahmed", "Fatima"]

# TUPLE -> Ordered, UNCHANGEABLE collection
# Used here for: Patient vital signs record (fixed, shouldn't change)
#if we use list so can change vitals aur agar vitals change so we can't treat patient efficiently jis ki wa ja se hospital ki rating pr effect ayega and vitals also could duplicate so we can't use here set and here is no key value pairs that's why we cant use dict  
# (heart_rate, blood_pressure_systolic, oxygen_level) recorded at admission
vitals_at_admission = (88, 120, 97)
print(f"Vitals recorded at admission (HR, BP, O2): {vitals_at_admission}")

heart_rate, bp_systolic, oxygen = vitals_at_admission


# SET -> Unordered collection with NO duplicates
# Used here for: Unique list of departments currently active in hospital
#we can't here use tuple bcz departments are change in every year or maybe month , and here order is not important so is lie list use na kri and keyvalue pairs bhu nhi thy is lue dict bhi use na hoi
departments_today = {"ICU", "Emergency", "General", "ICU", "Maternity", "Emergency"}

# DICTIONARY -> Key-Value pairs
# Used here for: Full patient profile (structured data lookup)
#if use set so we cn't use here duplicate value , if use tuple so we can't apply CRUD operation on it
patient_profile = {
    "name": "Ahmed",
    "age": 34,
    "department": "ICU",
    "vitals": vitals_at_admission,   # tuple stored inside dictionary
}
'''
Task 2
Ye code :
patients = ["Ali", "Ahmed", "Ali"]
blood_groups = {"A+", "O+", "A+"}
patient = {
    "name": "Ahmed",
    "age": 45
}
location = (24.86, 67.00)
Batana:
patients list kyun hai? bcz we change patients 
blood_groups set kyun hai? bcz blood group duplicate 
patient dictionary kyun hai? bcz here is complete one patient record
location tuple kyun hai? bcz location doesn't change 
Aur...
Agar sab ko list bana dein to kya problems hongi?
agar sb ko list banaden to 3 imapct paryn gyn blood groups main hamyn pata ni chalyga k kitny unique blood groups hyn haamary hospital main 
agar dict ko list baanden to index number se yaad rkhna paryga jo bht mushkil h agar kl ko koi nai value add krni pari to pora code toot jaayega
agar location ko list banaen to hoskta h kisi func k throw latitude aur longitude change hojaye aur loog ghalat location pr chaly jayen 
'''
'''
Task 3 (Engineer Thinking)

Tum AI Hospital bana rahe ho.
Neeche batao kaunsi collection use karoge aur kyun?
Hospital ke saare doctors ====> List, bcz changeable
Unique diseases   ===> set , bcz duplicate se bachao
Patient profile ===> dict, bcz key value pair
Hospital location ===> tuple bcz do not changeable
Appointment history ===> dict, bcz key value pair
Medicines prescribed ===> list, changeable
Emergency contacts ===> tuple, does not changeable
AI Model Configuration ===> set
Prediction Results ===> dict, 
Logged-in users ===> list
Har ek ke liye batao:
List?
Tuple?
Set?
Dictionary?
Aur sabse important:
"Agar galat collection choose kar di to system par kya impact padega?"
agar ghalat collection choose krdi to system ka code phat skta h 
'''
