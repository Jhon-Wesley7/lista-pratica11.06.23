from flask import Flask, render_template, redirect, request

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/lista-tarefas')
def lista_tarefas():
    print(tasks)
    return render_template('lista_tarefas.html', tasks=tasks)

@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        tarefa = request.form['tarefa']
        tasks.append(tarefa)
        return redirect('/lista-tarefas')
    return render_template('adicionar_tarefa.html')

@app.route('/concluir-tarefa/<int:task_id>')
def concluir_tarefa(task_id):
    if task_id < len(tasks):
        tasks[task_id] = f'[CONCLUÍDA] {tasks[task_id]}'
    return redirect('/lista-tarefas')

@app.route('/excluir-tarefa/<int:task_id>')
def excluir_tarefa(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect('/lista-tarefas')

if __name__ == '__main__':
    app.run(debug=True)