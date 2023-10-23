#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
username="admin"
password="12345"

while True:
    entered_username=input("enter your username:").strip()
    entered_password=input("enter your password:").strip()

    if entered_username==username and entered_password==password:
        print("login successful!")
        break
    else:
        print("invalid username or password try again.")
