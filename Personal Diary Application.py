def create_entry(filename, content):
    
    with open(filename, 'w') as file:
        file.write(content)

def read_entry(filename):
   
   
    try:
        with open(filename, 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print("No entry found for this date.")

def main_menu():
    print("Welcome to your Personal Diary App")

    while True:
        print("\nOptions:")
        print("1. Create a new entry")
        print("2. Read an existing entry")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter the date for your entry (YYYY-MM-DD): ")
            content = input("Write your entry below:\n")
            create_entry(f"{date}.txt", content)
            print("Entry saved.")

        elif choice == '2':
            date = input("Enter the date of the entry you want to read (YYYY-MM-DD): ")
            read_entry(f"{date}.txt")


            
        elif choice == '3':
            print("Exiting the diary app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
