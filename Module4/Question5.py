# correct username and password
correct_username = "python"
correct_password = "rules"

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts = attempts + 1
        if attempts == max_attempts:
            break
        print("Incorrect username or password. Please try again.")

if attempts == max_attempts:
    print("Access denied")
