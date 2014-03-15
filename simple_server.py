from flask import Flask
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('simple_server', 'templates'))

app = Flask(__name__)
app.debug = True
template = env.get_template('index.html')
@app.route("/")
def hello():
    print "here"
    return template.render(username='hi')

if __name__ == "__main__":
    app.run()
