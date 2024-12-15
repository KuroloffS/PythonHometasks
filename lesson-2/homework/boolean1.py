#lesson3 #boolean #problem1
def main():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username and password:
        print("Login successful!")
    else:
        print("Error: Both username and password must not be empty.")

if name == "main":
    main()