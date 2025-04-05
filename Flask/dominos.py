from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hi! Welcome to Dominos! How can I assist you today?",
    "order pizza": "Sure! We have Margherita, Pepperoni, and Veggie Supreme. What would you like to order?",
    "price": "Our pizzas range from $5 to $15 depending on the size and toppings.",
    "thanks": "You're welcome! Would you like anything else?",
    "bye": "Goodbye! Have a great day!"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message'].lower()
    response = responses.get(user_message, "Sorry, I didn't understand that. Can you please rephrase?")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
