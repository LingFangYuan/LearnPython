from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route('/<name>')
def hello_world(name):
    return 'Hello Ling! %s' % name


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        d = request.form
    else:
        d = {'phy': 59, 'che': 60, 'maths': 90}
    return render_template('hello.html', result=d, marks=10)


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/<int:id>')
def hello_flask(id):
    return 'Hello flask! %s' % id


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('hello_world', name=name))
    else:
        return redirect(url_for('hello_world', name='other'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('hello_world', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('hello_world', name=user))


@app.route('/')
def index():
    return render_template('login.html', name='ddddd')


if __name__ == '__main__':
    app.run(debug=True)
