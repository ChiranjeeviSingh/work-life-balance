from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib

from employee_form import EmployeeForm


# prediction function
def make_prediction(features_model, thepolymodel, svrmodel, sample_json):
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

    
    # Predict for 0 to 1
    arr_prep=features_model.fit_transform(employee)
    score = thepolymodel.predict(arr_prep)

    if score[0]<0 or score[0]>1:
        svr=svrmodel.predict(employee)
        return svr[0]

    else:
        return score[0]


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
ftr= joblib.load("models/features_model")
poly = joblib.load("models/thepolymodel")
svrr=joblib.load("models/svrmodel")


@app.route('/prediction')
def prediction():
    content = {'Gender': float(session['Gender']),
               'companyType': float(session['companyType']), 'WFHsetupavailable': float(session['WFHsetupavailable']),
               'Age': float(session['Age']),'Tenure': float(session['Tenure']),'vacationsTaken': float(session['vacationsTaken']),'Designation': float(session['Designation']),
               'avghourworkday': float(session['avghourworkday']),'employeeSatisfactionScore': float(session['employeeSatisfactionScore'])}

    results = make_prediction(ftr, poly, svrr, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
