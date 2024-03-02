from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/Needs', methods=['POST','GET'])
def Needs():
    if request.method == 'POST':
        first_name=request.form['First_name']
        last_name=request.form['Last_name']
        age=request.form['Age']
        contact_number=request.form['Contact_number']
        contact_number2=request.form['Contact_number2']
        requirement_name = request.form['Requirement_name']
        id1=request.form['Id1']
        proof_of_requirement=request.form['Id2']
        organization_location = request.form['Location']
        description=request.form['Description']


        mongo.db.Needs.insert_one({
            'first_name':first_name,
            'last_name':last_name,
            'age':age,
            'id1':id1,
            'requirement_name': requirement_name,
            'organization_location': organization_location,
            'contact_number': contact_number,
            'contact_number2':contact_number2,
            'proof_of_requirement': proof_of_requirement,
            'description':description
        })
        return redirect(url_for('Received'))
        
    return render_template('Needs.html')

@app.route('/Received')
def Received():
    return render_template('Received.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

# Inside app.py
@app.route('/details')
def details():
    contact_number = request.args.get('contact_number')
    data = mongo.db.Needs.find_one({'contact_number': contact_number})
    if data:
        return render_template('details.html', contact_number=contact_number, data=data)
    else:
        return "No data found for the provided contact number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
