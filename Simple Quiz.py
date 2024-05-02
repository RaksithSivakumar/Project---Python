quiz_questions = [
    ("What is the capital of France?", ["A) London", "B) Paris", "C) Berlin", "D) Madrid"], "B"),
    ("Which planet is known as the Red Planet?", ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], "C"),
    
]
asked_questions = set()

user_answers = {}

def ask_question():
    for i, (question, options, answer) in enumerate(quiz_questions):
        if i not in asked_questions:
            print(question)
            for option in options:
                print(option)
            user_input = input("Enter your answer (A, B, C, or D): ").upper()
            user_answers[i] = user_input
            asked_questions.add(i)
            break


def check_answers():
    score = 0
    for i, (_, _, answer) in enumerate(quiz_questions):
        if user_answers.get(i) == answer:
            score += 1
    return score

def play_quiz():
    while len(asked_questions) < len(quiz_questions):
        ask_question()
    final_score = check_answers()
    print(f"Quiz completed! Your final score is {final_score}/{len(quiz_questions)}")

play_quiz()
