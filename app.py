from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

tasks = []
tasks_id_control = 1

@app.route('/tasks', methods=['POST'])
def creat_task():
    global tasks_id_control
    data = request.get_json()
    new_task = Task(id=1,title=data['title'], description=data.get("description", ""))
    tasks_id_control += 1
    tasks.append(new_task)
    print(tasks)
    
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list, 
        "total_tasks": len(task_list)
  }
    return jsonify(output)
    


if __name__ == "__main__":
    app.run(debug=True)