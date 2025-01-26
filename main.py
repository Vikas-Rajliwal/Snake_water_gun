'''
1 for sanke 
-1 for water
0 for gun 

'''
import random

computer = random.choice([0,-1,1])
print("Enter from 's' ,'w','g'\ns:snake ,w:water,g: gun")
youestr= input("Enter your choice: ")
youDict={
    "s":1,"w":-1,"g":0
}
reverseDict={
    1:"snake",-1:"water",0:"Gun"
}
you =youDict[youestr]
print(f"Your choice {reverseDict[you]} \nComputer choice {reverseDict[computer]}")
you =youDict[youestr]
if(computer==you):
    print("Draw")
else:
    if (computer==-1 and you==1):
        print("you win!!!! ")
    elif(computer==-1 and you ==0):
        print("you loose!")    
    elif (computer==1 and you==-1):
        print("you loose! ")
    elif(computer==1 and you ==0):
        print("you win!!!!")    
    elif (computer==0 and you==-1):
        print("you win!!!! ")
    elif(computer==0 and you ==1):
        print("you loose!")    
  
    else:
        print("something went wrong") 
   
    
    