from flask import Flask, jsonify, render_template, request, redirect, url_for

print("🔥 RUNNING UPDATED app.py 🔥")

# ---------- APP INITIALIZATION ----------
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ---------- DATA (TEMP STORAGE) ----------
TASKS = [
    {"id": 1, "title": "Design UI", "assigned_to": "Frontend"},
    {"id": 2, "title": "Setup Backend", "assigned_to": "Backend"}
]

TEAMS = [
    {"id": 1, "name": "Team Alpha"},
    {"id": 2, "name": "Team Beta"}
]

# ---------- ROUTES (PAGES) ----------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks-page", methods=["GET", "POST"])
def tasks_page():
    if request.method == "POST":
        title = request.form.get("title")
        assigned_to = request.form.get("assigned_to")

        if title and assigned_to:
            TASKS.append({
                "id": len(TASKS) + 1,
                "title": title,
                "assigned_to": assigned_to
            })

        return redirect(url_for("tasks_page"))

    return render_template("tasks.html", tasks=TASKS)

@app.route("/teams-page")
def teams_page():
    return render_template("teams.html", teams=TEAMS)

# ---------- API ROUTES ----------
@app.route("/api/tasks")
def tasks_api():
    return jsonify({"tasks": TASKS})

@app.route("/api/teams")
def teams_api():
    return jsonify({"teams": TEAMS})

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
