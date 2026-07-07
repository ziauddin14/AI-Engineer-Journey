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
