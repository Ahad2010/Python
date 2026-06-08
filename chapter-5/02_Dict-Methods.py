marks = {
    "Ahad" : 100,
    "Ali" : 90,
    "Anaya" : 99
    }

print(marks.keys()) # Sab kwy return kre ga

print(marks.values()) # Sab vlaues return hogi

print(marks.items()) # key value pairs retrun
print(marks.get("name"))
print(marks.get("salary"))  # Error nahi dega


marks.update({"age": 21}) # Dictonary update  kre ga
print(marks)

marks.pop("Anaya") #remove kre ga
print(marks)

marks.popitem() #Lat item remove krega
print(marks)  

marks.clear() # Sab remove kr dega
print(marks)

new_student = marks.copy() # Copy krta hai