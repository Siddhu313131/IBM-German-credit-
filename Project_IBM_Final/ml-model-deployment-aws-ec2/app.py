from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x3 = request.form.get('x3')
    x4 = request.form.get('x4')
    x5 = request.form.get('x5')
    x6 = request.form.get('x6')
    x7 = request.form.get('x7')
    x8 = request.form.get('x8')
    x9 = request.form.get('x9')
    x10 = request.form.get('x10')
    x11 = request.form.get('x11')
    x12 = request.form.get('x12')
    x13 = request.form.get('x13')



    # prediction
    result = model.predict(np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13]).reshape(1,13))

    if result[0] == 1:
        result = 'LOAN APPROVED'
    else:
        result = 'LOAN NOT APPROVED'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4200)