from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def save_password(service, username, password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())

    with open("passwords.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password.decode()}\n")

def retrieve_password(service):
    key = load_key()
    f = Fernet(key)

    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                service_name, username, encrypted_password = line.strip().split(",")
                if service_name == service:
                    decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                    return f"Service: {service_name}, Username: {username}, Password: {decrypted_password}"
    return "Service not found!"

def main():
    if not os.path.exists("secret.key"):
        print("Generating encryption key...")
        generate_key()

    while True:
        print("\nPassword Manager")
        print("1. Add New Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            service = input("Enter the service (e.g., Gmail, Facebook): ")
            username = input("Enter the username/email: ")
            password = input("Enter the password: ")
            save_password(service, username, password)
            print("Password saved successfully!")
        
        elif choice == "2":
            service = input("Enter the service name to retrieve the password: ")
            print(retrieve_password(service))
        
        elif choice == "3":
            print("Exiting password manager.")
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
