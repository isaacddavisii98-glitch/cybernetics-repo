import datetime 
First_Name = input("What is your First name:") 
Last_Name = input(("What is your Last Name:"))
birth_year = int(input("What year were you born: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print("Hello " + First_Name + " " + Last_Name)


age = current_year - birth_year
print (f"You are ",int(current_year)-birth_year) 