from flask import Flask
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/hello")
def hello():
    return "hello world"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello, " + name + "!"

@app.route("/sum/<int:num1>/<int:num2>")
def add_numbers(num1, num2):
    return str(num1) + "+"+ str(num2) + "=" + str(num1 + num2)

@app.route("/greet/<name>")
def greet_name(name):
    return "안녕하세요, " + name + "님"

@app.route("/info")
def info_data():
    return "포트 : {0}/ 데이터 베이스 : {1}".format(config.PORT, config.DB_NAME)


@app.route("/hi")
def hi():
    return "hi world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
