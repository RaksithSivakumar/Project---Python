from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3000
PROTEIN_GOAL = 100

today = []

@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int

done = False

while not done:
    print("""
        (1) Add a new food
        (2) Visualize progress
        (3) Quit 
           """)
    
    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding a new food")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protein = int(input("Protein: "))
        fat = int(input("Fat: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, protein, fat, carbs)
        today.append(food)
        print("Successfully added!")
        
    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fat_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig, axs = plt.subplots(2, 2, figsize=(10, 10)) 
        axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Protein", "Fat", "Carbs"], autopct="%1.1f%%")
        axs[0, 0].set_title("Macronutrients Distribution")

        axs[0, 1].bar(["Calories"], [calorie_sum], color='blue')
        axs[0, 1].axhline(y=CALORIE_GOAL_LIMIT, color='red', linestyle='--')
        axs[0, 1].set_title("Calories Intake")
        axs[0, 1].set_ylim(0, CALORIE_GOAL_LIMIT + 500)
        axs[0, 1].text(0, CALORIE_GOAL_LIMIT + 20, 'Calorie Goal', color='red', ha='center')

        axs[1, 0].bar(["Protein"], [protein_sum], color='green')
        axs[1, 0].axhline(y=PROTEIN_GOAL, color='red', linestyle='--')
        axs[1, 0].set_title("Protein Intake")
        axs[1, 0].set_ylim(0, PROTEIN_GOAL + 50)
        axs[1, 0].text(0, PROTEIN_GOAL + 5, 'Protein Goal', color='red', ha='center')

        fig.delaxes(axs[1, 1])  

        plt.tight_layout()
        plt.show()
        
    elif choice == "3":
        done = True
        print("Goodbye!")
