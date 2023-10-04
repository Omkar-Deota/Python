# from flask import Flask,render_template, request
# import pandas as pd
# import pickle
# app=Flask(__name__)
# data=pd.read_json('columns.json')
# model=pickle.load(open('banglore_home_prices_model.pickle',"rb"));
# @app.route('/')
# def index():
#     locations=sorted(data['data_columns'].unique())
#     return render_template('index.html',locations=locations)
# @app.route('/predict',methods=['POST'])
# def predict():
#     locations=request.form.get('location')
#     bhk=request.form.get('bhk')
#     bath=request.form.get('bathroom')
#     sqft=request.form.get('total_sqft')
#     # print(locations,float(bhk),float(bath),sqft)
#     input=pd.DataFrame([[locations,sqft,bath.bhk]],columns=['location','total_sqft','bath','bhk'])
#     prediction=model.predict(input)[0]

#     return str(prediction+" Lakh")

# if __name__=="__main__":
#     app.run(debug=True,port=5001)

from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the data and model
data = pd.read_json('columns.json')
model = pickle.load(open('bengaluru_home_prediction', 'rb'))

@app.route('/')
def index():
    # Use 'data_columns' instead of 'data_columns' in your code
    locations = sorted(data['data_columns'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Use request.form.getlist to get multiple selected values for 'location' instead of request.form.get
    locations = request.form.getlist('location')
    bhk = float(request.form.get('bhk'))  # Convert to float
    bath = float(request.form.get('bathroom'))  # Convert to float
    sqft = float(request.form.get('total_sqft'))  # Convert to float

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({'location': locations, 'total_sqft': sqft, 'bath': bath, 'bhk': bhk})

    # Predict the price using the model
    prediction = model.predict(input_data)[0]

    return f"{prediction:.2f} Lakh"  # Format the prediction as a string with two decimal places

if __name__ == "__main__":
    app.run(debug=True, port=5001)
