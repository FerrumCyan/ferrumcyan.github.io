from flask import *
from imgtrans import *
app = Flask(__name__)

@app.route('/')
def index():
    old_url="static/images/che.jpeg"
    new_url="static/images/mononoke_che.jpeg"
    return render_template('index.html',urls=[old_url,new_url])
    
    
@app.route('/change',methods=["get","post"])
def change():
    obj=request.files.get("photo")
    old_name = obj.filename
    old_url = "static/images/"+old_name
    obj.save(old_url)
    
    style = request.values.get("style")

    new_name = style+"_"+old_name
    new_url = "static/images/"+new_name
    trans(old_url,style,new_url)
    
    return render_template('index.html',urls=[old_url,new_url])

app.run()