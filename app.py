from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': '1',
    'title': "Blood Needed",
    'Type': "O+",
    'Location': "Hyderabad, Sims Hospital"
}, {
    'id': '2',
    'title': "Money Needed",
    'Type': "Cancer Patient",
    'Location': "Guntur, Andhra Hospitals"
}, {
    'id': '3',
    'title': "Money Needed",
    'Type': "Old age House",
    'Location': "Hyderabad, Lahur Old Age Hospital"
}, {
    'id': '1',
    'title': "Blood Needed",
    'Type': "O+",
    'Location': "Amaravathi, Andhra Pradesh, Manipal Hospitals"
}]

@app.route("/home")
def home():
  return render_template('home.html')
  
@app.route("/")
def function():
  return render_template('index.html', jobs=JOBS)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
