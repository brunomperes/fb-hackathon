from flask import Flask, render_template, request, session, g, redirect, url_for, flash
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('simple_server', 'templates', 'static'))

app = Flask(__name__)
app.debug = True
template = env.get_template('index.html')
@app.route("/")
def hello():
    print "here"
    variable = url_for('static', filename='style.css')
    return template.render(username='hi')

if __name__ == "__main__":
    app.run()
