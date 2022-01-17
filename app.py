import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    #float_features = [float(x) for x in request.form.values()]
    #features = np.array(float_features).reshape(1,-1)
    if request.method == "POST":
        age = request.form['age']
        sex = request.form['sex']
        if sex == "Male":
            s = 0
        else:
            s = 1
        bmi = request.form['bmi']
        child = request.form['children']
        smoke = request.form['smoker']
        if smoke == "Yes":
            sm = 0
        else:
            sm =1 
    inputdata = [age,s,bmi,child,sm]
    input_data_as_numpy_arrar = np.asarray(inputdata).reshape(1,-1)
    input_data_as_numpy_arrar = input_data_as_numpy_arrar.astype(np.float)
    m = model.predict(input_data_as_numpy_arrar)
    print(m)

    return render_template("index.html", prediction_text= "{}".format(m))


if __name__ == "__main__":
    app.run(debug=True)