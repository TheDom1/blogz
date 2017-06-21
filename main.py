from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import traceback

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://blogz:password@localhost:8889/blogz'
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['GET','POST'])
def index():

    blogs = Blog.query.all()
    return render_template("blogs.html", blogs=blogs)

@app.route("/blog/<blog_id>", methods=['POST', 'GET'])
def indvidual_blogpost(blog_id):
    post = Blog.query.get(blog_id)
    print(post)
    print('6'*500)
    return render_template('individual_entry.html', title=post.title, post=post)



@app.route("/newblog", methods=['POST', 'GET'])
def index2():

    blogs = Blog.query.all()

    print(blogs)

    try:
        if request.method == 'POST':

            blog_body = request.form['blog_body']
            blog_name = request.form['blog_name']
            new_blog = Blog(blog_name, blog_body)
            db.session.add(new_blog)
            db.session.commit()
            blog_id = new_blog.id

            if not blog_body and blog_name:
                #render page with error.
                print('no blog body or name or something')
                
            return redirect('/?id={blog_id}'.format(blog_id=blog_id))


        else:


            return render_template('newblog.html', title="New Blog", blogs=blogs)

    except Exception:
        traceback.print_exc()
    



if __name__ == '__main__':
    app.run()
