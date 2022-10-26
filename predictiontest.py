import joblib
features_model = joblib.load('models/features_model')
themodel = joblib.load('models/thepolymodel')
svrmodel=joblib.load('models/svrmodel')

def predicted():
    g=int(input("gender: "))
    c=int(input("company: "))
    w=int(input("WFH: "))
    a=int(input("age: "))
    t=int(input("tenure in years: "))
    v=int(input("vacations taken: "))
    de=int(input("designation: "))
    avg=int(input("avg hours per day: "))
    ss=float(input("satistaction score out of 10: "))
    arr=[[g,c,w,a,t,v,de,avg,ss],[g,c,w,a,t,v,de,avg,ss]]
    
    mfg=themodel.predict(features_model.fit_transform(arr))
    score=mfg[0]
    
    mfg_svr=svrmodel.predict(arr)
    score_svr=mfg_svr[0]
    
    if score<0 or score>1:
        score=score_svr
    
    print("Your MFG is: ", score)
    print("")
    if score>0 and score<0.25:
        print("Excellent! you have low fatigue and are energetic. Keep up the good work !")
    elif score>=0.25 and score<0.5:
        print("You are energetic but have some fatigue accumulated. Practicing meditation or Yoga highly recommended !")
    elif score>=0.5 and score<0.75:
        print("Its not looking good. You are quite tired up! ")
        print("You have 2 options. One is to self help with Meditation and Yoga")
        print("Other is booking an appointment with specialist.")
        print("which one do you choose?")
    elif score>=0.75:
        print("OMG! your hardwork us apprecited but you need help ASaP!!")
        print("Book you specialist appointment immediately! ")
    

predicted()