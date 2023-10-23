##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
username="admin"
password="12345"
max_attempts=3
attempts=0

while attempts<max_attempts:
    entered_username=input("enter your username:").strip()
    entered_password=input("enter your password:").strip()

    if entered_username==username and entered_password==password:
        print("login successful!")
        break
    else:
        attempts+=1
        print("invalid username or password try again.")
    if attempts>=max_attempts:
        print("too many incorrect attempts. programe will end now.")
