#*********************COndition Statements********************
# Hospital Management System - Using if, elif, else in Real-World Scenarios

# ==========================================================
# SCENARIO 1: Patient Triage - Assigning Priority Level
# ==========================================================
patient_name = "Ahmed Khan"
severity_score = 8   # scale of 1-10 (10 = most critical)

if severity_score >= 9:  #Is if ka purpose ye h k priority level check kiya jay k agar patient ki severity score 9 se high ho to usko critical consider krky red zone main dala jaye agar ye condition na hoti to hm kabhi bhi critical patients ko nhi allocate krpaty
    priority = "CRITICAL - Immediate Attention (Red Zone)"
elif severity_score >= 6: # ye elif urgent konsy patients hyn unko check krny k liye lagay h agar ye na hota to 9  se neechy aly sary patiets ko norml consider kia jata 
    priority = "URGENT - Attend within 15 minutes (Yellow Zone)"
else:
    priority = "NON-URGENT - Routine Checkup (Blue Zone)" # Ye wala else na hota to normal patients ko track nhi kr paty sirf high a urgent ko hi dekh skty 
#Is condition main elif ka block chaly ga kiunk severity score 6 se ziyada h 8 h hamary case main is liye ye block chaly g acondition true hogai h else aur if ka block nhi chly ga 
# ==========================================================
# SCENARIO 2: Bed Allocation Based on Availability
# ==========================================================
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
