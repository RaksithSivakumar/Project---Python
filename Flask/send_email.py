from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()

    if not data or not 'subject' in data or not 'recipients' in data or not 'body' in data:
        return jsonify({"error": "Invalid data"}), 400

    subject = data['subject']
    recipients = data['recipients']  
    body = data['body']

    try:
        msg = Message(subject, recipients=recipients)
        msg.body = body
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
