from flask import Flask
app = Flask("app", static_folder="web/static", template_folder="web/templates")

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

app.run(host="localhost", port=8080)