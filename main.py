from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return """<h1>Api Prediction:</h1>
              <h2>1. Ad Investment to Sales Prediction.</h2>
              <hr>Add TV, Radio & Newspaper Investments on /api/v1/predict. <b>INT VALUES</b></hr>
              <hr></hr>
              <h2>2. New Data</h2>
              <hr>Add New Values of TV, Radio & Newspaper Investments AND Sales Results on /api/v1/retrain.</hr>       
              """

@app.route('/api/v1/predict', methods=['GET'])
def predict():
    tv = int(request.args['tv'])
    radio = int(request.args['radio'])
    newspaper = int(request.args['newspaper'])
    
    loaded_model = pickle.load(open('model.pkl', 'rb'))

    new_data = [tv, 
                radio, 
                newspaper]

    prediction = loaded_model.predict([new_data])
    return jsonify({'Prediction': round(prediction[0],2)})

# @app.route('/api/v1/retrain', methods=['POST'])
# def retrain():
#     sale = request.get_json()
#     tv = sale['tv']
#     radio = sale['radio']
#     newspaper = sale['newspaper']
#     sales = sale['sales']
#     return jsonify({'message': 'OK, Added New Data'})

if __name__ == '__main__':
    app.run(debug=True) 