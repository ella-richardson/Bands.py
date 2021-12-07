#Bruces and Sheilas
#2 procedures
#1-9, 0-9, 0-9, 0-9
#Bruces (right num right place)
#Sheilas (right num wrong place)
#NO REPEATING THE SAME NUMBER (Nice Try)
#If a num is a Bruce, it does not count as a Sheila
#Congratulations, you won in _ guesses
#No infinite loop
#First digit in answer/guess cannot be zero
import random
def chooseNum(L1,L2):         #Ella's code           
    num1=random.choice(L1)
    L2.remove(num1)
    goalnums.append(num1)
    num2=random.choice(L2)
    L2.remove(num2)
    goalnums.append(num2)
    num3=random.choice(L2)
    L2.remove(num3)
    goalnums.append(num3)
    num4=random.choice(L2)
    L2.remove(num4)
    goalnums.append(num4)
    ran_num=(str(num1)+str(num2)+str(num3)+str(num4))
    print(ran_num)
def Bruces_Sheilas():         #Bella's code
    if guessnums[1]==goalnums[1]:
        
    

    
print("Welcome to Bruces and Sheilas")    
print(" ")
list1=[1,2,3,4,5,6,7,8,9]        #Bella's code
list2=[0,1,2,3,4,5,6,7,8,9]
goalnums=[] 
blah=chooseNum(list1,list2)
print(goalnums)
guessnums=[]
guess=input("Please choose a 4 digit integer: ")
guessnums.append(guess[0])
guessnums.append(guess[1])
guessnums.append(guess[2])
guessnums.append(guess[3])
print(guessnums)
bruces=0
sheilas=0



