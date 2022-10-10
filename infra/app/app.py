from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', sum=0)

@app.route('/multiply', methods = ['POST'])
def multiply():
    data = request.form
    result = int(data['num1']) * int(data['num2'])
    return render_template('index.html', sum=result)

app.run(host='0.0.0.0', port=8080)