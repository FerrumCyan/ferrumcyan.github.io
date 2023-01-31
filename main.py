from flask import *
app = Flask(__name__)
#主页
@app.route("/")
def index():
    return render_template("/index.html")
#英文主页
@app.route("/en")
def index():
    return render_template("/English/index.htmll")

app.run()
