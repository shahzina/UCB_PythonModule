#activity 4

name = input("What is your name?")
country = input("Which country are you from?")
age = int(input("How old are you?"))
hourly_wage = int(input("What is your wage by the hour?"))

satisfied = bool(input("Are you satisfied with your work?"))

daily_wage = hourly_wage * 8

print ("The employee is " + name +", "+ str(age) + " from " + country + "and earns an hourly wage of "+str(hourly_wage))

print (f"The daily wage is {daily_wage} and the level of satisfaction is {satisfied}")


'''
OUTPUT
What is your name? alex
Which country are you from? vietnam
How old are you?25
What is your wage by the hour?15
Are you satisfied with your work?yes
The employee is  alex, 25 from  vietnamand earns an hourly wage of 15
The daily wage is 120 and the level of satisfaction is True
'''
