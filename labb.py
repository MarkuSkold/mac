


"""Programmet ska räkna ut volymen för en liksidig kub samt en liksidig tetrahedron
Liksidig = alla sidor lika långa
Ta in data från användaren och printa ut svaret
Tänk på enheter, bestäm en enhet ni tar in information i, t.ex cm
Då får ni också ut svaren i kubikcentimeter (cm3) 1000 cm3 = 1 liter
Eftersom programmet ska kunna räkna ut både en kub och en tetrahedron behöver ni låta användaren välja detta
Exakt utförande är upp till individen."""



def cube(length):
    return length*length*length
#Function that calculates the volume of the cube.     
def tetra(length):
     return length*length*length/6** .5
#funtion that calculates the volume of the tetrahydron. 

user_l = float(input("Hello, old buddy old pal.\nI will help you to calculate the volume of your object.\nCan you please enter the length in cm?"))
#Create variabel so I can use it in functions. Needs to be input about the length from user. Use float if the user enter decimals in the terminal. Use newline to make it easier to read for user. 

form = input("\n\nGreat! Now tell me the form of the figure. \nPlease enter 1 if it´s a Cube or 2 if it´s a tetrahedron")
#create variabel so i can use it in functions. Need to be input about the form. 

if form =="1":
    print(f"I think I got it right. If the length of one side is {user_l} cm then the cubes volume is", round(cube(user_l), 2),"cm^3")
elif form == "2":
    print(f"I think I got it right. If the length of one side is {user_l} cm then the tetraderons volume is", round(tetra(user_l),2),"cm^3")
else: 
    print("Sorry, can´t understand. Please try again.")
#use if statement to decide what function to use, cube or tetra. Use format.  


#Develop1-Can it also tell us how many milkpackages the volume is? 
#Develop2-Create a loop if the terminal doesn´t understand the length.


 




#if or true/false) statement for cube or tetrahedron.

#calculation of cube
#calculation of tetrahedron

#output to user
