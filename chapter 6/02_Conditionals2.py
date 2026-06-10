a = int(input("Enter your age: "))

if(a>18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering invalid Negative age")

elif(a==0):
    print("Your are entering 0 which is not a valid age")
else :
    print("you are not above the age of consent")
print("End of the program")