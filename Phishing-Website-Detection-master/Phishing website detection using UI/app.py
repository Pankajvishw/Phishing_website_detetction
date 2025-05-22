from flask import Flask,render_template,request

import FeatureExtraction
import pickle
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = FeatureExtraction.getAttributess(url)
        print(data)
        # model_path = os.path.join(os.path.dirname(__file__), 'xgb.sav')
        # RFmodel = pickle.load(open(model_path, 'rb'))
        RFmodel = pickle.load(open('xgb.sav', 'rb'))
        predicted_value = RFmodel.predict(data)
        print(predicted_value)
        if predicted_value == 0:    
            value = "Legitimate"
            return render_template("home.html",error=value)
        else:
            value = "Phishing"
            return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)