from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "<p>Hello! Click below</p> <button>Do Not Click Me</button>"

@app.route('/add/<x>')
def abc(x):
    return (x + " bye bye")

app.run(host="0.0.0.0", port=5001)
