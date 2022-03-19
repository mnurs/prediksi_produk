from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('modelregr.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    for x in request.form.values():
        total = x

    data = []
    data.append(int(total))
    
    prediction = model.predict([data])
    output = round(prediction[0][0], 2)

    return render_template('index.html', jumlah=output, total=total)

if __name__ == '__main__':
    app.run(debug=True)


