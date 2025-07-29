from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
CONTACT_FILE = os.path.join(DATA_DIR, 'contact_messages.json')

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as f:
        return json.load(f)

def save_project(new_project):
    path = os.path.join(DATA_DIR, 'projects.json')
    with open(path, 'r+') as f:
        data = json.load(f)
        data.append(new_project)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/personal')
def personal_info():
    return jsonify(load_json('personal.json'))

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'POST':
        data = request.get_json()
        if not all(k in data for k in ('title', 'description', 'tech_stack', 'link')):
            return jsonify({"error": "Missing fields"}), 400
        save_project(data)
        return jsonify({"message": "Project added successfully!"}), 201
    return jsonify(load_json('projects.json'))

@app.route('/api/skills')
def skills():
    return jsonify(load_json('skills.json'))

@app.route('/api/experience')
def experience():
    return jsonify(load_json('experience.json'))

@app.route('/api/education')
def education():
    return jsonify(load_json('education.json'))

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    if not all(k in data for k in ('name', 'email', 'message')):
        return jsonify({"error": "Missing fields"}), 400

    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'w') as f:
            json.dump([], f)

    with open(CONTACT_FILE, 'r+') as f:
        messages = json.load(f)
        messages.append(data)
        f.seek(0)
        json.dump(messages, f, indent=2)
        f.truncate()

    return jsonify({"message": "Message received"}), 201

if __name__ == '__main__':
    app.run(debug=True)
