from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("file1.html")

ab=[]
@app.route('/', methods=["POST"])
def a():
    # return 'Hello World!'
    # if request.method == "get":
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
