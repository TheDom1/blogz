from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config ["SQLALCHEMY_DATABASE_URI"] = "mysql + pymysql://Build-a-Blog:password@localhost:8889/Build-a-Blog"
app.config["SQLALCHEMY_ECHO = TRUE"]    
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.integer, primary_key = True)
    title = db.Column(db.String(40))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body 

@app.route('/blogs', methods=['GET'])
def index():

    blogs = Blog.query.all()
    return render_template("blogs.html", blogs=blogs)






@app.route('/', methods=['POST', 'GET'])
def index():





    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('Blog.html',title="Dom's Blog!", tasks=tasks)



