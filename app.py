from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load("reg.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Retrieve form data
            name = request.form["name"]
            company = request.form["company"]
            years_exp = float(request.form["years_experience"])

            # Predict salary
            prediction = model.predict(np.array([[years_exp]]))[0]

            return render_template("index.html", name=name, company=company, 
                                   years_experience=years_exp, prediction=round(prediction, 2))
        except:
            return render_template("index.html", error="Invalid input! Please enter a valid number.")

    # Ensure name and company have default values in GET requests
    return render_template("index.html", name="", company="", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
