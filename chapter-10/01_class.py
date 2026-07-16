class Employee:
    name = "Ahad"
    language = "Python" #This is a class attribute 
    Credits = 120000

harry = Employee()
harry.name = "Ahad" #This is a an object  attribute 
print(harry.name,harry.language,harry.Credits)    

Rohan = Employee()
Rohan.name = "Rohan Robinson"
Rohan.language = "JavaScript" #This is a an object  attribute 
Rohan.Credits = 150000
print(Rohan.name,Rohan.language,Rohan.Credits)    
