from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EmployeeForm(FlaskForm):
   # Days = StringField("Days")
    Gender = StringField("Gender")
    companyType = StringField("Company Type")
    WFHsetupavailable = StringField("WFH Setup Available")
    Age = StringField("Age")
    Tenure = StringField("Tenure")
    vacationsTaken = StringField("Vacations taken")
    Designation   = StringField("Designation")
    avghourworkday  = StringField("Average Hours worked per day")
    employeeSatisfactionScore = StringField("Employee satifaction score")
    

    submit = SubmitField("Predict")
