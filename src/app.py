from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder="templates", static_folder="../static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/teams")
def teams():
    return jsonify({
        "teams": [
            {"id": 1, "name": "Team Alpha"},
            {"id": 2, "name": "Team Beta"}
        ]
    })

@app.route("/tasks")
def tasks():
    return jsonify({
        "tasks": [
            {"id": 1, "title": "Design UI", "assigned_to": "Frontend"},
            {"id": 2, "title": "Setup Backend", "assigned_to": "Backend"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

@app.route("/tasks-page")
def tasks_page():
    tasks = [
        {"id": 1, "title": "Design UI", "assigned_to": "Frontend"},
        {"id": 2, "title": "Setup Backend", "assigned_to": "Backend"}
    ]
    return render_template("tasks.html", tasks=tasks)
