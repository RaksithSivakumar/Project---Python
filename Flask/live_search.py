from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Sample data to search from (in a real-world scenario, this could be a database)
data = [
    "Flask", "Django", "React", "Angular", "Vue", "Node.js", "Python", "JavaScript", "TypeScript",
    "HTML", "CSS", "SQL", "MongoDB", "Docker", "Kubernetes", "AWS", "Azure", "GCP"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        results = [item for item in data if query.lower() in item.lower()]
    else:
        results = []
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
