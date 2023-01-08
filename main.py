from flask import *
from getmusic import *
from getimg import *
from getmovie import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",img_list=img)
    
app.run()
