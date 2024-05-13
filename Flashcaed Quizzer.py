import random
from tkinter.messagebox import askquestion

questions = ["What is the capital of France?", "What is the square root of 16?", "Who wrote 'To Kill a Mockingbird'?"]

answers = {
    questions[0]: ("Paris", "London", "Berlin", "Madrid"),
    questions[1]: ("2", "3", "4", "5"),
    questions[2]: ("Harper Lee", "Mark Twain", "Ernest Hemingway", "William Faulkner")
}

asked_questions = set()

def quiz_user():
    while len(asked_questions) < len(questions):
        question = random.choice(questions)

        if question not in asked_questions:
            asked_questions.add(question)

            print(f"Question: {question}")
            for i, option in enumerate(answers[question], start=1):
                print(f"{i}. {option}")

            user_answer = input("Enter the number of your answer: ")
            correct_answer = answers[question][0]
            if answers[question][int(user_answer) - 1] == correct_answer:
                print("Correct!!")
            else:
                print(f"Incorrect! The correct answer is: {correct_answer}")
        else:
            continue
    
    print("Quiz completed!")

quiz_user()
