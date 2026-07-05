#*********************COndition Statements********************
# Hospital Management System - Using if, elif, else in Real-World Scenarios
# SCENARIO 1: Patient Triage - Assigning Priority Level
patient_name = "Ahmed Khan"
severity_score = 8   # scale of 1-10 (10 = most critical)

if severity_score >= 9:  #Is if ka purpose ye h k priority level check kiya jay k agar patient ki severity score 9 se high ho to usko critical consider krky red zone main dala jaye agar ye condition na hoti to hm kabhi bhi critical patients ko nhi allocate krpaty
    priority = "CRITICAL - Immediate Attention (Red Zone)"
elif severity_score >= 6: # ye elif urgent konsy patients hyn unko check krny k liye lagay h agar ye na hota to 9  se neechy aly sary patiets ko norml consider kia jata 
    priority = "URGENT - Attend within 15 minutes (Yellow Zone)"
else:
    priority = "NON-URGENT - Routine Checkup (Blue Zone)" # Ye wala else na hota to normal patients ko track nhi kr paty sirf high a urgent ko hi dekh skty 
#Is condition main elif ka block chaly ga kiunk severity score 6 se ziyada h 8 h hamary case main is liye ye block chaly g acondition true hogai h else aur if ka block nhi chly ga 

# SCENARIO 2: Bed Allocation Based on Availability
department = "ICU"
available_beds = {
    "ICU": 2,
    "General": 15,
    "Emergency": 0,
    "Maternity": 5
}

beds_left = available_beds.get(department, 0)

if department == "ICU" and beds_left == 0: # YE condition CHECK KRYGI K DEPT BHI ICU HONA CHAHIYE AUR BED LEFT BHI 0 K EQUL HON TAB YE TRU HOGI AUR CONDITOIN RUN HOGI AGAR YE CONDITION HATADEN TO code pr KOI IMPACT NHI PARYGA 
    allocation = "No ICU beds available. Transfer to nearest hospital recommended."
elif department == "ICU" and beds_left > 0: #CONDITION AGAR HATADEN TO SECOND LAST CONDITION TRU HOJAYEGI AGAR NHI HATAEN TO ORDER KA LIHZA KRTY HOYE YE WALI CONDITION TRU HOGI AUR BAQI TEEN BLOCK HOOJAYEN GIN
    allocation = f"ICU bed allocated. {beds_left} bed(s) remaining."
elif beds_left == 0:
    allocation = f"No beds available in {department}. Patient added to waiting list."
elif beds_left <= 3:
    allocation = f"Bed allocated in {department}. Low availability ({beds_left} left) - notify admin."
else:
    allocation = f"Bed allocated in {department}. {beds_left} beds remaining."

print(f"Department Requested: {department}")
print(f"Result: {allocation}")

'''
#Task 2
Is code ko dekho:
temperature = 39
if temperature >= 40:
    status = "Critical"
elif temperature >= 38:
    status = "High Fever"
else:
    status = "Normal"
Batana:
if ka purpose? 
TEMP K  40 K EQUL YA USSE ZIYADA HONY K BEHAVE PR STATUS RECOGNIZE KRNY K LIYE 
elif ka purpose?
HIGH FEVER WALON KO DETECT KRNY K LIYE
else ka purpose?
NORMALS KO DKEHNY K LIYE
Agar elif hata dein to kya hoga?
AGAR HATADEN TO 40 SE NEECHY JINKA BHU TEMP HOGA WO NORMAL CONSIDER KIYE JAYEN GYN AUR KUCH AISE PATIENTS HOSKTY HYN JINKO HIGH FEVER HOTA AUR WO ELIF NAHONY KI WAJA SE NORMAL MAIN CHALY JATY DR KI UNSE NAZAR HATY AUR WO DEATH KA SHIKAR NAA HOJAYEN CRITICAL CONDITION HOJAYEGI
Agar temperature = 41 ho to output kya hoga aur kyun?
AGAR TEM 39 KI JAGA 41 HO TO STATUS CIRICAL HOGA KIUN K IF KI CONDITION TRUE HOJAYEGI BAQI BLLOCKS OF ODE FREEZ HOJAYEGN
'''

'''
Task 3 (Engineer Thinking)

Tum AI Hospital bana rahe ho.
Neeche diye gaye scenarios ke liye batao:
Kis jagah sirf if use hoga aur kyun?
Kis jagah if-else use hoga aur kyun?
Kis jagah if-elif-else use hoga aur kyun?

Scenarios:
Patient admitted hai ya nahi.
IF ELSE KIUN K YAHAN BHI 2 CONDITIONS HYN
Patient ka fever: Normal, High, Critical.
IF ELIF ELSE KIUN K YAHAN TEEN CONDITIONS HYN 
Bill paid hua ya nahi.
IF ELSE KIUN K DO CONDITIONS HYN 
Sugar level: Low, Normal, High, Emergency.
IF ELIF ELIF ELSE KIUN K YAHAN 4 CONDITIONS CHECK HONGIN
Login successful ya failed.
IF ELSE DONON CONDIION CHECK HOGI 
'''

#******************************Loops****************************
"""
Hospital Management System - Loop Concepts Demo (3 Scenarios)
Covers: for loop, while loop, break, continue
"""
# SCENARIO 1: FOR LOOP + BREAK -> Find first available ICU bed

icu_beds = {
    "Bed-1": "Occupied",
    "Bed-2": "Occupied",
    "Bed-3": "Available",
    "Bed-4": "Occupied",
    "Bed-5": "Available"
}

for bed, status in icu_beds.items():   #Yahan for loop lagany ka purpse ye h k k for dictionery k hr item pr jakr check kryga k staus avaliabe h ya nhi agra nhi to automatic next ite pr move hojayega agar ye loop na lagaty to manually jakr hr item pr condition laga laga kr check krna parta k  bed avaliable h ya nhi jisse time kharab hota hoskta h jis patient kko bed chahiye wo critical condition main ho usko k aagr foran treatment naho bed na milny ki waja se to wo maar skta h 
    if status == "Available":
        print(f"Bed found: {bed} is available. Assigning patient now.")
        # break -> stop searching once first available bed is found
        break #yahan is condition pr break lagay k agar condition true hojaye jis item pr bhi to loop ieediatly ruk jaye kiun k loop ka purpose khatma hogya hospital ko ye chekc krna tha k in sary beds main se avaliable bed konsa h jese hi mila loop ruk jaye aaagy print krna ek irrelevent meaning less print hoga jiska koi faida nhi agar ye break na lagaye hatadn
    print(f"{bed} is occupied, checking next bed...")
print()

# SCENARIO 2: FOR LOOP + CONTINUE -> Skip discharged patients

patient_status = {
    "Ali": "Admitted",
    "Sara": "Discharged",
    "Ahmed": "Admitted",
    "Fatima": "Discharged",
    "Zain": "Admitted"
}

for name, status in patient_status.items(): #apply for loop for iteration on each item of dict if not apply so manually chek krna paryga jisse time kharab hoga 
    if status == "Discharged":
        # continue -> skip this patient, move to next one
        continue # discharged patients ko skipo krny k liye  ye loop lagany ka purpose hi discharge patients ko skip krnyk liye tha agar ye nhi lagaty to purpose hi pora naa hota 
    print(f"Preparing medication schedule for: {name} (Status: {status})")
print()

# SCENARIO 3: WHILE LOOP + BREAK -> Emergency queue processing
emergency_queue = ["Accident Victim", "Chest Pain Patient", "Fracture Case",
                    "CRITICAL: Cardiac Arrest", "Minor Injury"]

while emergency_queue: #While use kiya kiun k yahan pr pata nhi h emergency queue kitni dafa h kia h agar ye nhi lagaty for lagaty to ye 5 6 dafa chal kr ruk jata kbky is loop ka purpose h k jb tk critical case wali emergency queue detectna ho tb tk rukna nhi h
    current_case = emergency_queue.pop(0)  # take next patient from queue
    print(f"Attending to: {current_case}")

    if "CRITICAL" in current_case:
        print("CRITICAL case detected! Rushing to Operation Theater immediately.")
        # break -> stop processing queue, handle emergency directly
        break

print("Remaining queue paused due to critical case override.")

'''
Task 2
Ye code dekho:
patients = ["Ali", "Ahmed", "Critical", "Sara"]
for patient in patients:

    if patient == "Critical":
        break

    print(patient)
Batana:
for ka purpose?
list k hr tem ko bari bari check krna
break ka purpose?
condiiton true hony pr loop ko roook dena
Output kya hoga?
Ali, Ahmed, Critical
Agar break hata dein to kya hoga?
agar break hataden to critical patient nhi mily ga jiski waja se loop lagaya gaya tha loop lagny ka purpse tha k critical patient mil jaye taky uky sath treatment start kiya jaye ab agar critical hatadneto ye end ittem tk loop chala jayega jismain criticalk missing hony ka khadsha h 
'''
'''
Task 3 (Engineer Thinking)
Tum AI Hospital bana rahe ho.
Neeche batao kis situation mein kya use hoga aur kyun?
100 patients ki reports ek ek karke check karni hain.
for use hoga kiun k iteration maaloom h 
Doctor ke online aane tak wait karna hai.
while use hoga kiun k iteration maaloom nhi
Corrupted patient record skip karna hai.
continue use hoga kiun k recor skip krna h loop khatm nhi krna
Emergency patient milte hi scanning rok deni hai.
break use hoga kiun k emergency milty hi scanning rook kr loop khatam krnA h 
Har doctor ke saare patients print karne hain.
Nested loop bcz doctors pr ek loop chalyga phir hr docotr k hr hr patient pr alag se ek nested loop chala kr print krn hoga ek looop lagayem gyn to sirf docotrs print hongy
Batana:
for
while
break
continue
Nested Loop
Kahan use hoga aur kyun.
'''
