from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_database, get_all_todos, add_todo, toggle_todo, delete_todo, update_todo, get_todo_by_id

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # for messages

# Run the database at application startup
@app.before_request
def create_tables():
    init_database()

@app.route("/")
def index():
    todos = get_all_todos()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task = request.form.get("task")
        priority = int(request.form.get("priority", 1))

        # Data verification
        if task and task.strip():
            add_todo(task.strip(), priority)
            flash("The task was successfully added!", "success")
            return redirect(url_for("index"))
        else:
            flash("Please enter the task text!", "error")

    return render_template("add.html")

@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        flash("The task does not exist!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task and new_task.strip():
            update_todo(todo_id, new_task.strip())
            flash("The task has been successfully updated!", "success")
            return redirect(url_for("index"))
        else:
            flash("Please enter the task text!", "error")

    return render_template("edit.html", todo=todo)

@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    toggle_todo(todo_id)
    flash("The mission status has changed!", "info")
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    delete_todo(todo_id)
    flash("The task has been deleted!", "warning")
    return redirect(url_for("index"))

@app.route("/filter/<status>")
def filter_tasks(status):
    todos = get_all_todos()
    if status == "completed":
        todos = [todo for todo in todos if todo['done']]
    elif status == "pending":
        todos = [todo for todo in todos if not todo['done']]

    return render_template("index.html", todos=todos, current_filter=status)

if __name__ == "__main__":
    app.run(debug=True)
