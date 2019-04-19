from flask import Flask, render_template, request

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


engine = create_engine(os.getenv("postgres://jypthddpgzkyyv:41eaa68d8f4d665a3d27f4c5d7f1d1f3ff80d9652de2f52b35b0c28a788c9662@ec2-54-83-205-27.compute-1.amazonaws.com:5432/d8dd3keevdr4gq"))

db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return render_template("file1.html")

ab=[]
@app.route('/', methods=["POST"])
def a():
    # return 'Hello World!'
    # if request.method == "get":

    #     aaa = db.execute().fetchall()
        n=request.form.get("name")
        # print(n)/
        ab.append(n)
        return render_template("file1.html",headline=ab)
    # return render_template("file1.html")

@app.route('/file2')
def file2():
    # return 'Hello World!'
    return render_template("file2.html")

# if __name__ == '__main__':
#     app.run(debug = True)
