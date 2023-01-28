from flask import *
app = Flask(__name__)
#主页
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/框架")
def index():
    return render_template("Basic.html")
#VIP{
@app.route("/a")
def index():
    return render_template("indexvip1.html")
}
app.run()
