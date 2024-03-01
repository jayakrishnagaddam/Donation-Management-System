from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"
app.config['MONGO_URI'] = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Donations"

mongo = PyMongo(app)

@app.route("/home")
def home():
    return render_template('home.html')
  
@app.route("/")
def function():
    return render_template('index.html')

@app.route('/donatepage')
def donatepage():
   
    emergencies_data = mongo.db.Emergency.find()
    return render_template('donatepage.html', Emergency=emergencies_data)

@app.route('/contactus')
def contact():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
