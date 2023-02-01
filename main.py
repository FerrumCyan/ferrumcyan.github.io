from flask import *
app = Flask(__name__)
#主页
@app.route("/")
def index():
    return render_template("/index.html")
#英语
@app.route("/en")
def en():
    return render_template("/en.html")

app.run()
