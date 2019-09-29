import pickle
from sklearn.externals import joblib

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)


joblib.dump(lin_reg, "linear_regression_model.pkl")

with open("python_lin_reg_model.pkl", "wb") as file_handler:
    pickle.dump(lin_reg, file_handler)
    
with open("python_lin_reg_model.pkl", "rb") as file_handler:
    loaded_pickle = pickle.load(file_handler)
    
loaded_pickle



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            years_of_experience = float(data["yearsOfExperience"])
            
            lin_reg = joblib.load("./linear_regression_model.pkl")
        except ValueError:
            return jsonify("Please enter a number.")

        return jsonify(lin_reg.predict(years_of_experience).tolist())

joblib.dump(train_set, "training_data.pkl")
joblib.dump(train_labels, "training_labels.pkl")

@app.route("/retrain", methods=['POST'])
def retrain():
    if request.method == 'POST':
        data = request.get_json()

        try:
            training_set = joblib.load("./training_data.pkl")
            training_labels = joblib.load("./training_labels.pkl")

            df = pd.read_json(data)

            df_training_set = df.drop(["Salary"], axis=1)
            df_training_labels = df["Salary"]

            df_training_set = pd.concat([training_set, df_training_set])
            df_training_labels = pd.concat([training_labels, df_training_labels])

            new_lin_reg = LinearRegression()
            new_lin_reg.fit(df_training_set, df_training_labels)

            os.remove("./linear_regression_model.pkl")
            os.remove("./training_data.pkl")
            os.remove("./training_labels.pkl")

            joblib.dump(new_lin_reg, "linear_regression_model.pkl")
            joblib.dump(df_training_set, "training_data.pkl")
            joblib.dump(df_training_labels, "training_labels.pkl")

            lin_reg = joblib.load("./linear_regression_model.pkl")
        except ValueError as e:
            return jsonify("Error when retraining - {}".format(e))

        return jsonify("Retrained model successfully.")