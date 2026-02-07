from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = int(request.form["age"])
        gender = request.form["gender"]
        bp = float(request.form["blood_pressure"])
        sugar = float(request.form["sugar_level"])

        # Validation
        if age < 0:
            return render_template("index.html", error="Age cannot be negative!")

        # Simple risk logic (no ML encoding problem)
        risk_score = 0

        if age > 45:
            risk_score += 20
        if bp > 130:
            risk_score += 30
        if sugar > 140:
            risk_score += 40

        risk_percentage = min(risk_score, 100)

        if risk_percentage >= 70:
            risk_level = "High Risk"
            color = "red"
            doctor_tips = [
                "Consult a doctor immediately",
                "Reduce sugar and salt intake",
                "Avoid junk food and smoking",
                "Do regular health checkups"
            ]
        elif risk_percentage >= 40:
            risk_level = "Medium Risk"
            color = "orange"
            doctor_tips = [
                "Exercise daily for 30 minutes",
                "Eat fruits and vegetables",
                "Monitor BP and sugar levels",
                "Reduce stress"
            ]
        else:
            risk_level = "Low Risk"
            color = "green"
            doctor_tips = [
                "Maintain a healthy lifestyle",
                "Drink enough water",
                "Continue regular exercise",
                "Do yearly health checkups"
            ]

        return render_template(
            "index.html",
            prediction=risk_level,
            risk_percentage=risk_percentage,
            color=color,
            tips=doctor_tips
        )

    except:
        return render_template("index.html", error="Please enter compilation values correctly!")

if __name__ == "__main__":
    app.run(debug=True)
