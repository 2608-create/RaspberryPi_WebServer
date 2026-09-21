from flask import Flask
import config

app = Flask(__name__)

@app.route("/sum/<int:a>/<int:b>")
def sum_two(a, b):
    return "{0} + {1} = {2}".format(a, b, a + b)


@app.route("/greet/<name>")
def greet(name):
    return "안녕하세요, {0}님".format(name)


@app.route("/info")
def info():
    return "포트 : {0} / 데이터베이스 : {1}".format(config.PORT, config.DB_NAME)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
