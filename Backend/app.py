from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/simplify", methods=["POST"])
def simplify():
    data = request.get_json()
    report = data.get("report", "").lower()

    if not report:
        return jsonify({"result": "No report provided."})

    if "blood sugar" in report or "hba1c" in report:
        result = "Blood sugar levels are high. This may indicate diabetes risk."
    elif "cholesterol" in report:
        result = "Cholesterol levels appear elevated. Heart health risk detected."
    elif "creatinine" in report or "egfr" in report:
        result = "Kidney function indicators are abnormal."
    elif "hemoglobin" in report or "wbc" in report:
        result = "Blood test values suggest possible anemia or infection."
    else:
        result = "Report analyzed. No major abnormalities detected."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
