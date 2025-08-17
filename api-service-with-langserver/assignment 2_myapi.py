from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for tasks
tasks = [
    {"id": 1, "title": "Do the laundry", "completed": False},
    {"id": 2, "title": "Finish assignment", "completed": True}
]

@app.route("/")
def home():
    """Root endpoint with API description."""
    return jsonify({
        "message": "Welcome to the Task Manager API!",
        "endpoints": {
            "/tasks": "Get a list of tasks",
            "/tasks/<task_id>": "Get details of a specific task"
        }
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get the list of tasks."""
    return jsonify({"tasks": tasks})

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get details of a specific task."""
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)