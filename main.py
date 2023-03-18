welcome_prompt = "Welcome Doctor, what would you like to do?\n-Press 1 to list all patients.\n-Press 2 to run a new diagnosis.\n-Press q to quit.\n"

name_prompt = "What is the patient's name?\n"
Appearance_prompt = " How is the patient's genearal appearance?\n-1: Normal appearance\n-2: Irritable or Lethargic\n" 


def ListAll():
    print("Listing all patients\n")

def assess_eyes():
   print("Assessing eyes.\n")

def assess_skin():
    print("Assessing skin.\n")

def AskAppearance():
    appearance = input(Appearance_prompt)    
    if appearance == "1":
      assess_eyes()
    elif appearance == "2":
      assess_skin()
    else:
        print("Invalid value.\n")

def RunDiagnosis():
    name = input(name_prompt)
    AskAppearance()

def main():
    
    while(True):

      selection = input(welcome_prompt)
      if selection == "1":
       ListAll()
      elif selection == "2":
            RunDiagnosis()
      elif selection == "q":
         return
      else:
         print("Invalid value.\n")       
        



main()