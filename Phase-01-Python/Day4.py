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
