
def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark, mysterious cave. Do you enter?")
    choice = input("Enter 'yes' to go inside or 'no' to walk away: ").lower()

    if choice == 'yes':
        cave_entrance()
    elif choice == 'no':
        print("You decide to stay safe and walk away. Maybe another adventure awaits you.")
    else:
        print("That's not a valid choice. Let's try this again.")
        start_adventure()

def cave_entrance():
    print("\nYou cautiously step into the cave. It's dark and you can hear distant echoes.")
    print("After walking for a few minutes, you come across a fork in the path.")
    choice = input("Do you go 'left' or 'right'?: ").lower()

    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("You hesitate and the moment passes. Let's try this again.")
        cave_entrance()

def left_path():
    print("\nYou take the left path and find a treasure chest!")
    print("Do you open it?")
    choice = input("Enter 'open' to reveal the treasure or 'leave' to continue exploring: ").lower()

    if choice == 'open':
        print("You found a treasure full of gold and jewels! You're rich!")
    elif choice == 'leave':
        print("You leave the chest untouched and continue on your adventure.")
    else:
        print("That's not a choice. The chest remains closed as you ponder.")
        left_path()

def right_path():
    print("\nYou take the right path and encounter a sleeping dragon!")
    print("Do you try to sneak past it?")
    choice = input("Enter 'sneak' to move quietly or 'run' to dash past the dragon: ").lower()

    if choice == 'sneak':
        print("You sneak past the dragon and find an exit out of the cave. You've made it!")
    elif choice == 'run':
        print("You run with all your might but awaken the dragon. It's time to face your fate!")
    else:
        print("Indecision is sometimes worse than the wrong decision. The dragon stirs.")
        right_path()

start_adventure()
