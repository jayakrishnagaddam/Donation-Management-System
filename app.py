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
        requirement_name = request.form['Requirement_name']
        patient_name = request.form['Patient_name']
        organization_location = request.form['Location']
        contact_number = request.form['Contact_number']
        proof_of_requirement = request.form['Proof']
        
        # Save proof_of_requirement to a folder or cloud storage and get its URL
        
        # Insert the data into MongoDB
        mongo.db.Needs.insert_one({
            'requirement_name': requirement_name,
            'patient_name': patient_name,
            'organization_location': organization_location,
            'contact_number': contact_number,
            'proof_of_requirement': proof_of_requirement  # You can replace this with the URL
        })
        return redirect(url_for('donatepage'))
        
    return render_template('Needs.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
