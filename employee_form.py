from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EmployeeForm(FlaskForm):
   # Days = StringField("Days")
    Gender = StringField("Gender 0: Male, 1: Female")
    companyType = StringField("Company Type 0: Service, Product: 1")
    WFHsetupavailable = StringField("WFH Setup Available 0: No, 1: Yes")
    Age = StringField("Age")
    Tenure = StringField("Tenure (in years)")
    vacationsTaken = StringField("Vacations Taken per Year(in days)")
    Designation   = StringField("Designation (enter b/w 1 to 5)")
    avghourworkday  = StringField("Average Hours worked per day")
    employeeSatisfactionScore = StringField("Employee satifaction score 1 to 10")
    

    submit = SubmitField("Predict")
