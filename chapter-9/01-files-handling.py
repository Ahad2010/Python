correct_user = "Ahad"
correct_password = 123456

user = input("Enter user: ")
password = int(input("Enter password: "))  # Convert input to int to match

if user == correct_user and password == correct_password:
    print("Login success")
else:
    print("Not found")