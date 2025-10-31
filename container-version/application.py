from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

todo_items = []  # in-memory task list
edit_task_index = None  # tracks index being edited

@application.route('/')
def home():
    global edit_task_index
    return render_template('home.html', items=todo_items, edit_index=edit_task_index)

@application.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_items.append(task)
    return redirect(url_for('home'))

@application.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todo_items):
        todo_items.pop(index)
    return redirect(url_for('home'))

@application.route('/edit/<int:index>')
def edit(index):
    global edit_task_index
    if 0 <= index < len(todo_items):
        edit_task_index = index
    return redirect(url_for('home'))

@application.route('/update/<int:index>', methods=['POST'])
def update(index):
    global edit_task_index
    updated_task = request.form.get('updated_task')
    if updated_task and 0 <= index < len(todo_items):
        todo_items[index] = updated_task
    edit_task_index = None
    return redirect(url_for('home'))

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)