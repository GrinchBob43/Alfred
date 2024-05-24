from flask import Flask

app = Flask(__name__)


@app.route("/walter")
def hello_walter():
    return "Hello Walter!"


@app.route("/")
def hello():
    return "Go away!"

@app.route("/say_hello/<name>")
def say_hello(name="no name"):
    return f"Hello, {name}. I hope you're having a productive day."

if __name__ == "__main__":
    app.run(debug=True)