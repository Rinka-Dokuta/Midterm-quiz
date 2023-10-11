for i in range (6, 39, 3):
    print (i, end = " ")
    
print()

calories = int(input("How many minuets of exercise do you get every week?"))
if calories < 20:
    print("That's not enough exercise!")
elif calories < 100:
    print("Get a bit more exercise!")
elif calories < 500:
    print("That's the perfect amount of exercise! Good job!")
else:
    print("That's alot! Make sure you get enough water and protein")
    
print()

from winsound import Beep

def Beep():   
    Beep(440, 500)
   
num = int(input("Please type a number"))

#I don't know how to use while like this
