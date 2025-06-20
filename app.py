from flask import Flask, request, render_template_string

app = Flask(__name__)
tasks = []

HTML = '''
<h1>Simple ToDo App</h1>
<form method="POST">
    <input name="task" placeholder="Enter task">
    <input type="submit" value="Add">
</form>
<ul>
    {% for t in tasks %}
        <li>{{ t }}</li>
    {% endfor %}
</ul>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template_string(HTML, tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
