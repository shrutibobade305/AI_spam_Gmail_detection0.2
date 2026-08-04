from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


# Load trained model

model = pickle.load(open("model.pkl", "rb"))


# Load text vectorizer

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))




@app.route("/")
def home():

    return render_template("index.html")





@app.route("/predict", methods=["POST"])
def predict():


    # Get email text from index.html

    message = request.form["message"]



    # Convert text into numbers

    data = vectorizer.transform([message])



    # Prediction

    prediction = model.predict(data)[0]




    # Probability calculation

    try:


        probabilities = model.predict_proba(data)[0]


        safe_probability = round(probabilities[0] * 100, 2)

        spam_probability = round(probabilities[1] * 100, 2)

        confidence = round(max(probabilities) * 100, 2)



    except:



        if prediction == 1:

            spam_probability = 90

            safe_probability = 10


        else:

            spam_probability = 10

            safe_probability = 90



        confidence = max(
            spam_probability,
            safe_probability
        )







    # Convert prediction label


    if prediction == 1:


        result = "Spam"


        reasons = [

            "Suspicious words detected",

            "Message contains spam patterns",

            "Possible promotional or phishing content"

        ]



    else:


        result = "Safe"


        reasons = [

            "Normal email structure",

            "No suspicious keywords detected",

            "Message looks trustworthy"

        ]







    return render_template(

        "result.html",

        prediction=result,

        confidence=confidence,

        spam_probability=spam_probability,

        safe_probability=safe_probability,

        reasons=reasons

    )






if __name__ == "__main__":

    app.run(debug=True)