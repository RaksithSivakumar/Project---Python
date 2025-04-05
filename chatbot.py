
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! What's on your mind?",
    "how are you": "I'm doing well, thanks! How about you?",
    "what's your name": "My name is Chatty, nice to meet you!",
    "goodbye": "Goodbye! It was nice chatting with you.",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "default": "I didn't understand that. Can you please rephrase?"
}

def get_user_input():
    return input("You: ")

def respond(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

def tell_joke():
    import random
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

def fun_fact():
    import random
    facts = [
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896, and lasted only 38 minutes.",
        "The longest word in the English language, according to the Oxford English Dictionary, is pneumonoultramicroscopicsilicovolcanoconiosis, a lung disease caused by inhaling very fine particles of silica.",
        "Butterflies taste with their feet.",
        "A group of flamingos is called a 'flamboyance'.",
        "The human nose can detect over 1 trillion different scents."
    ]
    return random.choice(facts)

def main():
    print("Welcome to Chatty!")
    while True:
        user_input = get_user_input()
        response = respond(user_input)
        print("Chatty: " + response)
        
        if "joke" in user_input:
            print("Chatty: " + tell_joke())
        elif "fun fact" in user_input:
            print("Chatty: " + fun_fact())
        elif "help" in user_input:
            print("Chatty: I can respond to greetings, tell jokes, provide fun facts, and more! Try asking me something.")
        
        if user_input.lower() == "goodbye":
            break

main()