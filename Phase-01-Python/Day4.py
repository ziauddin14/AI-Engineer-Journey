#***************Exception Handling*******************
'''
Ye code dekho:
try:
    sugar = int(input("Sugar Level: "))

    if sugar < 0:
        raise ValueError("Invalid Sugar")

except ValueError:
    print("Invalid Input")

else:
    print("Prediction Started")

finally:
    print("Log Saved")
Batana:
try ka purpose? ==> for risky code
except ka purpose? ==> for handling error 
else kab chalega? ==> jab risky code gracefully execute hojaye
finally kab chalega? ==> chahyn user shi inout daly ya ghalat input daly
raise kyun use hua?==> agar koi user negative value daly to usko handle krny k liye 
Agar raise hata dein to system par kya impact padega?  ==> agar raise hataden to system main negative values of suger aajayegn gin jiski waja se patient ko ghalat treatment mil skta h jisse uski jaan ko khatra hoskta h 
'''
'''
Task 3 (Engineer Thinking)
Tum AI Hospital bana rahe ho.
Neeche batao kis situation mein kaunsi exception handle karoge aur kyun:
User ne age ki jagah "abc" likh diya. ==> valueError except age galat dali gai to us age k according patient ok treatment nhi milyga 
Doctor ne patient ki report upload nahi ki. ==>raise valueError hoga patient ki current report upload nhi ki to uski current condition ka pata nhi lag skyga
AI model file missing hai. 
Database disconnect ho gaya.
User negative weight likhta hai. raise ValueError kiun k weight galat hoga to masly hoskt hyn 
API timeout ho gaya. 
User image ki jagah PDF upload kar deta hai. ===> raise valueerror
Har case mein batao:
Kis type ka error ho sakta hai?
try, except, finally ya raise mein se kya use karoge?
Business impact kya hoga agar handle na kiya?
'''
"""
Hospital Management System - Exception Handling Demo
Covers: try, except, else, finally, raise
Author: Zia's AI Engineer Journey - Phase 01 (Python)
"""

def admit_emergency_patient(name, heart_rate, department):
    #try -> for risky code
    try: 
        print(f"\nProcessing emergency admission for: {name}")

        # raise -> manually trigger an error if data is medically invalid
        if heart_rate <= 0:
            raise ValueError(f"Invalid heart rate reading: {heart_rate}")

        beds = available_beds[department]   # may raise KeyError if department invalid

        if beds == 0:
            raise Exception(f"No beds available in {department}. Cannot admit patient.")

    except ValueError as ve:
        print(f"Medical data error: {ve}")
    except KeyError:
        print(f"Department error: '{department}' does not exist.")
    except Exception as e:
        print(f"Admission failed: {e}")
    else:
        # else -> runs only if admission succeeded with no errors
        available_beds[department] -= 1
        print(f"{name} admitted successfully to {department}. Beds remaining: {available_beds[department]}")
    finally:
        # finally -> always runs, success or failure
        print(f"Admission process completed for: {name}")


#********************File Handling*****************
'''
Task 2 (Concept)
Ye code dekho:
with open("report.txt", "w") as file:
    file.write("Patient Stable")
    
Batana:
with ka purpose? for closing file automatically
open() ka purpose? for opening file
"w" kyun use hua? for identifying file mode
file.write() kya karta hai? for writing in the file
close() kahaan hua? automaticaly with the help of with keyword
Agar "a" use karte to kya difference hota? porana data bhi rehta aur Patient Stable file k last main jaa kr add hojata 
Agar "r" use karte aur file exist na karti to kya ho sakta hai? error aajata
'''

'''
Task 3 (Engineer Thinking)
Tum AI Hospital bana rahe ho.
Neeche batao kis cheez ko file mein save karoge aur kyun:
Patient Reports --> a mode (agar w mode use kiya to previous reports chali jayegn gin)
AI Predictions --> r mode
Chatbot Conversations a mode (agar w mode use kiya to porani conversation ka data chala jayega jisse cahtbot pata hi nhi laga payega k user kia baaat kr rha tha )
Error Logs  w mode
Doctor Notes a mode
Daily Revenue a mode
Appointment History a mode
Har item ke liye batao:
Kis mode (r, w, a) ka use zyada hoga?
Agar galat mode choose kar diya to business par kya impact padega?
'''

"""
Hospital Management System - File Handling Demo
Covers: open(), "r", "w", "a", close(), with open()
Author: Zia's AI Engineer Journey - Phase 01 (Python)
"""
# SCENARIO 5: FULL FLOW -> Daily discharge log system

discharged_today = ["Ahmed - Recovered", "Sara - Transferred to General"]

# Step 1: Write today's discharge log (overwrite old log with "w")
with open("discharge_log.txt", "w") as file:
    file.write("=== Discharge Log ===\n")
    for entry in discharged_today:
        file.write(entry + "\n")
print("Step 1: New discharge log created.")

# Step 2: A late discharge comes in -> append it with "a"
with open("discharge_log.txt", "a") as file:
    file.write("Zain - Discharged (late entry)\n")
print("Step 2: Late discharge appended to the log.")

# Step 3: Read back the final log to confirm everything is correct
with open("discharge_log.txt", "r") as file:
    print("\nStep 3: Final discharge log:")
    print(file.read())


#*********************Module & Packeges****************************
'''
Task 1: 5 Modules (Hospital Project)
patients.py
- register_patient()
- update_patient()
- delete_patient()
- search_patient()
Purpose: Patient ka data (naam, age, disease, admission info) manage karne ke liye. Ye module sirf patient records ke CRUD (Create, Read, Update, Delete) operations handle karega.
doctors.py
- add_doctor()
- assign_doctor_to_patient()
- update_doctor_schedule()
- remove_doctor()
Purpose: Doctors ki info aur unki availability/schedule manage karna, aur patients ko doctors assign karna.
billing.py
- generate_bill()
- add_payment()
- calculate_discount()
- print_invoice()
Purpose: Patient ke treatment ka financial hisaab rakhna — bill banana, payment track karna, discounts apply karna.
appointments.py
- book_appointment()
- cancel_appointment()
- reschedule_appointment()
- get_appointment_list()
Purpose: Patient aur doctor ke beech appointment scheduling manage karna.
inventory.py
- add_medicine()
- update_stock()
- check_expiry()
- remove_medicine()
Purpose: Hospital ki medicine/equipment stock ka record rakhna, taake shortage ya expiry ka pata chal sake.
Agar sab code ek hi file mein likhein to kya problems hongi?

Readability kharab ho jayegi — Sab functions ek jagah hone se dhoondna mushkil ho jayega ke generate_bill() kahan hai.
Maintenance mushkil — Agar billing mein bug fix karna ho, tumhe pura file scroll karna padega, aur risk hai ke accidentally kisi aur function ko chhu do.
Team collaboration impossible — Agar 5 log alag modules pe kaam karna chahein, ek hi file pe sab likhne se merge conflicts (Git mein) bohot zyada honge.
Reusability khatam — Agar sirf billing logic kisi doosre project mein use karna ho, tumhe pura mixed file uthana padega, sirf ek clean module nahi.
Naming clashes — Agar do modules mein galti se same naam ka function ban gaya (jaise dono mein update()), to conflict/overwrite ho sakta hai.
Testing complicated — Har feature ko individually test karna mushkil ho jata hai jab sab ek doosre se mixed ho.

Ye exactly wahi reason hai jiske wajah se AI engineering mein bhi hum code ko modules mein todte hain — jaise RAG pipeline mein retriever.py, embedder.py, generator.py alag hote hain, sab kuch ek main.py mein nahi hota.

Task 2: Import Concepts
pythonimport math
from math import sqrt
import random as rnd

print(math.pi)
print(sqrt(25))
print(rnd.randint(1, 5))

import ka purpose: Kisi bhi built-in ya external module (jisme pehle se likha hua code/functions hain) ko apni file mein use karne ke liye load karna. Isse tumhe wheel dobara invent nahi karni padti.
from ... import ... ka purpose: Pure module ko load karne ke bajaye, usme se sirf ek specific function/cheez nikaal ke lena. Jaise from math import sqrt — pura math load nahi ho raha naam se, sirf sqrt function directly mil raha hai.
as ka purpose: Module ko ek chhota/custom naam (alias) dena, taake baar baar lamba naam na likhna pade. import random as rnd ke baad tum random.randint() ki jagah rnd.randint() likh sakte ho — shorter aur convenient.
math.pi kya hai: Ye math module ke andar predefined ek constant value hai (3.14159...), jo function nahi hai — isliye bina brackets () ke access hota hai.
sqrt() direct kaise chal gaya: Kyunki tumne from math import sqrt likha tha — is line ne sqrt function ko direct current namespace mein la diya. Isliye math.sqrt() likhne ki zaroorat nahi, sirf sqrt() kaafi hai.
rnd kyun use hua: Kyunki import random as rnd se alias bana diya gaya tha. Ab jahan bhi random module ka koi function chahiye, rnd naam se access hoga — rnd.randint(1, 5).
Agar import math hi na likhen to kya hoga: print(math.pi) line pe NameError: name 'math' is not defined aayega, kyunki Python ko pata hi nahi ke math naam ka koi module exist karta hai jab tak explicitly import na kiya jaye. Note: sqrt(25) tab bhi chalta rahega kyunki wo from math import sqrt se already alag se import ho chuka hai — ye dikhata hai ke import math aur from math import sqrt do independent imports hain.


Task 3: AI Hospital — Module Design (Engineer Thinking)
Ye real system-design thinking hai — matlab tum ek professional AI engineer ki tarah decide kar rahe ho ke code ko kaise organize karna hai.
1. patients.py — Patient Management

Functions: register_patient(), update_patient(), get_patient_history(), delete_patient()
Why separate: Ye "core data" hai jise baaki har module (billing, AI prediction, chatbot) use karega. Isay clean rakhna critical hai.

2. billing.py — Billing System

Functions: generate_invoice(), apply_insurance(), process_payment(), refund()
Why separate: Financial logic sensitive hoti hai — isay alag rakhne se audit aur security control easy hota hai.

3. ai_prediction.py — AI Prediction

Functions: predict_disease_risk(), train_model(), load_model(), evaluate_prediction()
Why separate: Ye ML/AI logic hai — computationally heavy aur alag dependencies (numpy, sklearn, etc.) use karta hai. Isay patient ya billing logic se mix karna galat design hai.

4. chatbot.py — Chatbot

Functions: handle_user_query(), generate_response(), escalate_to_human()
Why separate: Ye ek conversational interface layer hai — LLM/API calls involve karta hai, jo baaki business logic se completely different concern hai.

5. database.py — Database

Functions: connect_db(), save_record(), fetch_record(), close_connection()
Why separate: Ye ek "shared utility layer" hai jise har module use karega. Alag rakhne se database engine change karna (SQLite se PostgreSQL) baaki code touch kiye bina possible hota hai.

6. auth.py — Authentication

Functions: login(), logout(), verify_token(), check_permissions()
Why separate: Security-critical code hai. Isay isolate karna zaroori hai taake access-control bugs baaki system ko affect na karein.

7. notifications.py — Email/SMS Notifications

Functions: send_email(), send_sms(), notify_appointment_reminder()
Why separate: Ye ek "external service integration" hai (third-party APIs jaise Twilio/SendGrid) — is tarah ke external dependencies ko isolate karna best practice hai.

8. reports.py — Report Generator

Functions: generate_patient_report(), generate_financial_summary(), export_pdf()
Why separate: Ye "read-only, output-focused" logic hai jo baaki modules ka data combine karke present karta hai — isay alag rakhna reporting logic ko baaki business logic se decouple karta hai.

Agar sab kuch main.py mein likh diya to business aur development par impact:

Scalability ruk jayegi: Jaise jaise hospital system grow karega (naye features add honge), file itni badi ho jayegi ke koi bhi developer usay samajh nahi payega.
Bug fixing risky ho jayega: Ek chhoti si billing change AI prediction ya chatbot ko accidentally break kar sakti hai, kyunki sab kuch tightly coupled hai.
Team scaling impossible: Real hospital software mein alag teams (backend, AI, security) parallel kaam karti hain. Ek file mein sab kuch hone se ye parallel kaam karna impossible ho jata hai.
Deployment aur testing slow: Chhota sa change bhi pura system retest karwayega, jo business ke liye time aur cost dono barhata hai.
Security risk: Authentication logic agar billing/chatbot code ke saath mixed ho, to attack surface badh jata hai — security review mushkil ho jata hai.

Yehi exact reasoning hai jo real AI engineering projects mein use hoti hai — jab tum aage LangChain ya FastAPI seekhoge, wahan bhi tum routes/, services/, models/ jaisi modular structure banaoge, exactly isi principle par.
Claude is AI and can make mistakes. Please double-check responses.
'''
