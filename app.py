from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib

from employee_form import EmployeeForm


# prediction function
def make_prediction(model, encoder, sample_json):
    # parse input from request
    #Days = sample_json['Days']
    Gender = sample_json['Gender']
    companyType = sample_json['companyType']
    WFHsetupavailable = sample_json['WFHsetupavailable']
    Age = sample_json['Age']
    Tenure = sample_json['Tenure']
    vacationsTaken = sample_json['vacationsTaken']
    Designation = sample_json['Designation']
    avghourworkday = sample_json['avghourworkday']
    employeeSatisfactionScore = sample_json['employeeSatisfactionScore']
    # Make an input vector
    employee = [[Gender, companyType, WFHsetupavailable,Age,Tenure,vacationsTaken,Designation,avghourworkday,employeeSatisfactionScore],[Gender, companyType, WFHsetupavailable,Age,Tenure,vacationsTaken,Designation,avghourworkday,employeeSatisfactionScore]]

    arr_prep=model.fit_transform(employee)
    # Predict
    prediction_raw = encoder.predict(arr_prep)

    # Convert Species index to Species name
    #prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_raw[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/", methods=['GET','POST'])
def index():
    form = EmployeeForm()

    if form.validate_on_submit():
        #session['Days'] = form.Days.data
        session['Gender'] = form.Gender.data
        session['companyType'] = form.companyType.data
        session['WFHsetupavailable'] = form.WFHsetupavailable.data
        session['Age'] = form.Age.data
        session['Tenure'] = form.Tenure.data
        session['vacationsTaken'] = form.vacationsTaken.data
        session['Designation'] = form.Designation.data
        session['avghourworkday'] = form.avghourworkday.data
        session['employeeSatisfactionScore'] = form.employeeSatisfactionScore.data
        
        return redirect(url_for("prediction"))
    return render_template("home.html", form=form)


# Read models
classifier_loaded = joblib.load("models/features_model")
encoder_loaded = joblib.load("models/themodel")


@app.route('/prediction')
def prediction():
    content = {'Gender': float(session['Gender']),
               'companyType': float(session['companyType']), 'WFHsetupavailable': float(session['WFHsetupavailable']),
               'Age': float(session['Age']),'Tenure': float(session['Tenure']),'vacationsTaken': float(session['vacationsTaken']),'Designation': float(session['Designation']),
               'avghourworkday': float(session['avghourworkday']),'employeeSatisfactionScore': float(session['employeeSatisfactionScore'])}

    results = make_prediction(classifier_loaded, encoder_loaded, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
