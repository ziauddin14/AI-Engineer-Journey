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

#*********************Strings*******************
"""
Hospital Chatbot - Common Python String Methods Demo
Author: Zia's AI Engineer Journey - Phase 01 (Python)
"""
# 1. .strip() -> Removes extra spaces from user input , if remove this method a lot of raw data aajayega DB main jisse Performance ya response pr effect aaskta h 
print("\n--- 1. .strip() : Cleaning User Input ---")
raw_input_text = "   I have fever   "
cleaned_input = raw_input_text.strip()
print(f"Raw input:     '{raw_input_text}'")
print(f"Cleaned input: '{cleaned_input}'")

# 2. .lower() / .upper() -> Case-insensitive matching if remove this method so chatbot will be confused which input is correct....?
print("\n--- 2. .lower() / .upper() : Case-Insensitive Matching ---")
user_message = "I Have FEVER and HEADACHE"
normalized = user_message.lower()
print(f"Original:   {user_message}")
print(f"Lowercased: {normalized}")

if "fever" in normalized:
    print("Chatbot: Detected symptom -> Fever. Recommending General Physician.")

# 3. .split() -> Breaking a sentence into words/symptoms if we not using this method chatbot can't identify what is symptoms actually in sentence...?
print("\n--- 3. .split() : Extracting Symptoms from Sentence ---")
symptom_sentence = "fever, headache, cough"
symptom_list = symptom_sentence.split(",")
# Clean each symptom of extra spaces after splitting
symptom_list = [symptom.strip() for symptom in symptom_list]
print(f"Sentence: {symptom_sentence}")
print(f"Extracted symptoms list: {symptom_list}")

# 4. .join() -> Combining a list back into a readable sentence if not using thsi method user can'y recognize which symptoms are actually I told to chatbot...?
print("\n--- 4. .join() : Formatting Symptoms for Display ---")
formatted_symptoms = ", ".join(symptom_list)
print(f"Chatbot: You reported these symptoms -> {formatted_symptoms}")

# 5. .replace() -> Correcting or masking chatbot text if user make typo mistake chatbot can't recognize what exactly word are using user....?
print("\n--- 5. .replace() : Correcting Common Typos ---")
user_typo = "I have feveer and heaadche"
corrected = user_typo.replace("feveer", "fever").replace("heaadche", "headache")
print(f"Original (typo):  {user_typo}")
print(f"Corrected:        {corrected}")

# 7. .find() -> Locating a keyword's position in a sentence if not using this method user can't identify which word are I exactly find in this massage 
print("\n--- 7. .find() : Locating Keyword Position ---")
patient_message = "My oxygen level is dropping and I feel dizzy"
position = patient_message.find("oxygen")
print(f"Message: {patient_message}")
print(f"'oxygen' keyword found at index: {position}")

if position != -1:
    print("Chatbot: Oxygen-related concern detected -> Flagging as URGENT.")

'''
Task 2
Ye code dekho.
patient_name = "  Ahmed Khan  "
print(patient_name.strip())  ===> removing extra spaces from text 
print(patient_name.upper()) ===> converting to uppercase
print(patient_name.lower()) ====> converting to lowercase
report = "Patient has Diabetes"
print(report.replace("Diabetes", "Hypertension")) ==> replacing the symptoms
print(report.split()) =====> splitting text into list
Batana.
strip() ka purpose?
upper()?
lower()?
replace()?
split()?
Aur.
Har method remove kar dein to real hospital system mein kya problem hogi?
clean text nhi milyga, 
chatbot ko hr tarah ka spelling parhan nhi ayega jisse response main effect aaskta h 
agar replace nhi lagaen to incorrect ko correct kese kryngyn user ko maza nhi ayega jisse wo negative feedback dekr chatbot aur hospitl ki rating gira skta h
split ka smjh nhi aaya kia hoskt h agar haatdn shayad ye hoskta h k symptoms ko recognize kiya ja skta h sentence ko split krky....
'''

'''
1. User extra spaces likhta hai
Method: .strip()
Kyun: User input ke shuru aur end mein extra spaces aksar hote hain (jaise "   fever   "), jo string comparison ko fail kar sakte hain.
Business Impact: Agar strip na kare, to "fever" == "  fever  " False aayega, aur chatbot symptom ko detect hi nahi kar payega — jisse patient ko galat ya koi response na milne ka risk hai. Ye ek silent bug hai jo user ko pata bhi nahi chalega, lekin system fail ho jayega.
2. User CAPITAL letters mein likhta hai
Method: .lower()
Kyun: Users kabhi "FEVER", kabhi "Fever", kabhi "fever" likhte hain — case matching consistent nahi hoti.
Business Impact: Agar sirf exact match check karo bina lower kiye, to chatbot "FEVER" ko symptom recognize nahi karega jabke wahi "fever" hai — jisse patient ko galat treatment suggestion mil sakta hai ya emergency case miss ho sakta hai. Case-insensitivity real accuracy issue hai, sirf cosmetic nahi.
3. Report mein disease search karni hai
Method: .find() ya in operator (aur bade documents ke liye aage jaake regex)
Kyun: Poori report ek lambi string hoti hai, aur humein pata karna hai ke koi specific disease keyword usme mention hua hai ya nahi, aur kaha (kis position pe).
Business Impact: .find() return karta hai keyword ki exact position — is se system disease ke around ka context bhi nikal sakta hai (jaise severity, date). Agar sirf in use karein, to sirf "hai ya nahi" pata chalega, position nahi — jo detailed medical report analysis ke liye kaafi nahi hota.
4. Patient ka full naam first aur last name mein todna hai
Method: .split()
Kyun: "Ahmed Ali Khan" jaisi string ko individual parts mein todhna hai taake first name aur last name alag se store/use ho sakein.
pythonfull_name = "Ahmed Ali Khan"
parts = full_name.split()
first_name = parts[0]
last_name = parts[-1]
Business Impact: Database mein first name aur last name alag columns mein store karna hota hai (proper record-keeping ke liye), aur formal letters/emails mein sirf last name (jaise "Dear Mr. Khan") use karna hota hai. Agar split na karein, to poora naam ek block treat hoga aur ye personalization possible nahi hogi.
5. Doctor ka naam display karna hai
Method: .title()
Kyun: Database mein naam kisi bhi format mein aa sakta hai ("dr. ahmed khan", "DR AHMED KHAN"), lekin display karte waqt professional aur consistent format chahiye.
Business Impact: Agar .title() na use karein, to UI pe inconsistent naam formatting dikhegi — jo unprofessional lagega aur patient trust ko affect karega. Ek chhoti si cheez, lekin brand perception pe direct impact.
6. File .csv hai ya .json check karna hai
Method: .endswith()
Kyun: Filename ke extension se pata chalta hai ke file kaunse format mein hai, taake sahi parser (CSV reader vs JSON parser) use ho.
pythonif file_name.endswith(".csv"):
    # process as CSV
elif file_name.endswith(".json"):
    # process as JSON
Business Impact: Agar file type galat detect ho, to system wrong parser use karega aur crash ho jayega ya corrupt data read karega — ye especially important hai jab tum patient records ya lab reports automatically process kar rahe ho (jaise tumhare future RAG/data pipeline mein).
7. Prompt mein "emergency" word hai ya nahi check karna hai
Method: in operator (with .lower() combined)
pythonif "emergency" in user_prompt.lower():
    print("URGENT: Flagging as emergency case!")
Kyun: Ye sabse critical check hai is puri list mein — humein sirf ye jaanna hai ke keyword present hai ya nahi, uski position ya count matter nahi karti.
Business Impact: Ye life-critical hai. Agar "emergency" detect na ho (case-sensitivity ki wajah se, ya extra spaces ki wajah se), to system us patient ko normal priority queue mein daal dega jabke unhe turant attention chahiye thi. Isliye yaha .lower() aur in dono ka combination zaroori hai — kabhi bhi is check ko halka mat lena.
'''



