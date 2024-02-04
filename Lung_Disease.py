from flask import Flask,render_template,request
import pandas as pd
import pickle


app=Flask(__name__)
data=pd.read_csv(r'C:\Users\ATHUL AKSHAY\Desktop\LUNG CANCER PREDICTION\survey lung cancer.csv')
model=pickle.load(open('lung_disease1.pkl','rb'))

@app.route('/')
def data():
    return render_template('lung_disease.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        age=int(request.form['age'])
        gender=request.form['gender']
        smoking=request.form['smoking']
        yellowfingers=request.form['yellowfingers']
        anxiety=request.form['anxiety']
        peerpressure=request.form['peerpressure']
        fatigue=request.form['fatigue']
        chronicdisease=request.form['chronicdisease']
        allergy=request.form['allergy']
        wheezing=request.form['wheezing']
        alcoholconsuming=request.form['alcoholconsuming']
        coughing=request.form['coughing']
        shortnessofbreath=request.form['shortnessofbreath']
        swallowingdifficulty=request.form['swallowingdifficulty']
        chestpain=request.form['chestpain']

        prediction=model.predict([[age,gender,smoking,yellowfingers,anxiety,peerpressure,fatigue,chronicdisease,allergy,wheezing,alcoholconsuming,coughing,shortnessofbreath,swallowingdifficulty,chestpain]])
        prediction=prediction[0]
        if prediction==0:
            p='YES'
        elif prediction==1:
            p='NO'
        
        return render_template('lung_disease.html',predict=p)
    
if __name__=='__main__':
    app.run(debug=True)
