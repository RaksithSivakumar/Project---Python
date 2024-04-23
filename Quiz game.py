print("Welcome to my Quiz!")
playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Okay! Let's play :) ")

answer = input("Which of the following is hardware? ").lower()
if answer == "monitor":
    print('Correct!')
else:
    print("Incorrect")

answer = input("Which of the following is software? ").lower()
if answer == "microsoft word":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What do you call the brain of the computer? ").lower()
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
else:
    print("Incorrect")

answer = input("Which of the following is an example of an operating system? ").lower()
if answer == "microsoft windows":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What does BIOS stand for? ").lower()
if answer == "basic input/output system":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What is the function of the hard disk drive? ").lower()
if answer == "storage":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What is another word for applications? ").lower()
if answer == "programs":
    print('Correct!')
else:
    print("Incorrect")

answer = input("Reducing a window until it becomes a button on the taskbar is called? ").lower()
if answer == "minimize":
    print('Correct!')
else:
    print("Incorrect")

answer = input("What term describes the process of making software's source code available to everyone? ").lower()
if answer == "open-source":
    print('Correct!')
else:
    print("Incorrect")
