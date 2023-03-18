welcome_prompt = "Welcome Doctor, what would you like to do?\n-Press 1 to list all patients.\n-Press 2 to run a new diagnosis.\n-Press q to quit.\n"

name_prompt = "What is the patient's name?\n"
Appearance_prompt = " How is the patient's genearal appearance?\n-1: Normal appearance\n-2: Irritable or Lethargic\n" 

eye_prompt = "How are the patients' eyes?\n-1: Eyes normal or slightly sunken\n-2: Eyes very sunken.\n"

skin_prompt = "How is the patient's skin when you pinch it?\n-1: Normal skin pinch\n-2: Slow skin pinch.\n"


severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydraiton = "No dehydration"
patients_and_diagnoses = [ ]



def list_patients():  
    for patient in patients_and_diagnoses:
       print(patient)

def save_new_diagnosis(name,diagnosis):  
   final_diagnosis = name + ":" + diagnosis
   patients_and_diagnoses.append(final_diagnosis)
   print("Final diagnosis:",final_diagnosis,"\n")      

def assess_eyes(eyes):
    if eyes == "1":
      return no_dehydraiton
    elif eyes == "2":
     return severe_dehydration
   

def assess_skin(skin):
    if skin == "1":
      return no_dehydraiton
    elif skin == "2":
     return severe_dehydration

def assess_appearance():
    appearance = input(Appearance_prompt)    
    if appearance == "1":
      eyes = input(eye_prompt)
      return assess_eyes(eyes)
    elif appearance == "2":
      skin = input(skin_prompt)
      return assess_skin(skin)
    else:
        print("Invalid value.\n")

def RunDiagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name,diagnosis)

def main():
    
    while(True):

      selection = input(welcome_prompt)
      if selection == "1":
       list_patients()
      elif selection == "2":
            RunDiagnosis()
      elif selection == "q":
         return
      else:
         print("Invalid value.\n")       
        


main()