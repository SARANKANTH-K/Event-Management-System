from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users2.db'
db = SQLAlchemy(app)


class users2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.String(15))
   
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
  
    # dob = db.Column(db.String(10))
    # gender = db.Column(db.String(10))
    # address = db.Column(db.String(200))
    # city = db.Column(db.String(50))
    # state = db.Column(db.String(50))

@app.route("/")
def login():
    return render_template("FrontLogin.html")

@app.route("/FrontLogin.html")
def FrontLogin():
    return render_template("FrontLogin.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/blocks.html")
def blocks():
    return render_template("blocks.html")

@app.route("/halls.html")
def halls():
    return render_template("halls.html")


@app.route("/Eventreg.html")
def Eventreg():
    return render_template("Eventreg.html")

@app.route("/RegisterEvent.html")
def RegisterEvent():
    return render_template("RegisterEvent.html")

@app.route("/admin.html")
def admin():
    return render_template("admin.html")

@app.route("/cc.html")
def cc():
    return render_template("cc.html")

@app.route("/maha.html")
def maha():
    return render_template("maha.html")

@app.route("/sri.html")
def sri():
    return render_template("sri.html")

@app.route("/ck.html")
def ck():
    return render_template("ck.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/FrontLogin",methods=['POST','GET'])
def form():
    try:
        if request.method == 'POST':
            
            name = request.form['adminfname']
            contact = request.form['admincontact']
            email = request.form['adminsignupemail']
            password = request.form['adminsignuppass']
        
           
        
            existing_user = users2.query.filter_by(username=name).first()
            if existing_user:
                message='Username is already exists'
                return render_template("FrontLogin.html",message=message)
            


            new_user = users2(username=name,contact=contact,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("FrontLogin.html")


    except Exception as e:
       print(e)
    return render_template("FrontLogin.html")

@app.route("/feedback.html")
def form2():
    return render_template("feedback.html")


if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True)





