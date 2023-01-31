from flask import *
app = Flask(__name__)
#主页
@app.route("/")
def index():
    return render_template("/index.html")

app.run()
