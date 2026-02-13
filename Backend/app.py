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
    report_text = data.get("report", "").lower()
    language = data.get("language", "en")  # default English

    if not report_text.strip():
        return jsonify({"result": "No medical report was provided."})

    # -------- Simplified explanations (English) --------
    if "blood sugar" in report_text or "hba1c" in report_text:
        result_en = (
            "Your blood sugar levels are higher than normal. "
            "This means your body may not be managing sugar efficiently. "
            "Maintaining a healthy diet, regular exercise, and consulting a doctor "
            "can help you manage this condition."
        )
        result_hi = (
            "आपके रक्त में शर्करा का स्तर सामान्य से अधिक है। "
            "इसका मतलब है कि शरीर शुगर को सही तरीके से नियंत्रित नहीं कर पा रहा है। "
            "संतुलित आहार, नियमित व्यायाम और डॉक्टर से सलाह लेना मददगार हो सकता है।"
        )

    elif "cholesterol" in report_text:
        result_en = (
            "Your cholesterol levels appear higher than recommended. "
            "High cholesterol can affect heart health over time. "
            "Eating healthy foods, staying active, and regular health checkups "
            "can help improve these levels."
        )
        result_hi = (
            "आपका कोलेस्ट्रॉल स्तर सामान्य से अधिक है। "
            "लंबे समय तक अधिक कोलेस्ट्रॉल हृदय स्वास्थ्य को प्रभावित कर सकता है। "
            "स्वस्थ आहार, सक्रिय जीवनशैली और नियमित जांच से इसमें सुधार हो सकता है।"
        )

    elif "creatinine" in report_text or "egfr" in report_text:
        result_en = (
            "Some values related to kidney function are outside the normal range. "
            "This suggests that the kidneys may not be working at full efficiency. "
            "Proper hydration, medication review, and medical consultation are advised."
        )
        result_hi = (
            "किडनी से जुड़े कुछ मान सामान्य सीमा से बाहर हैं। "
            "इसका मतलब है कि किडनी पूरी क्षमता से काम नहीं कर रही हो सकती है। "
            "पर्याप्त पानी पीना और डॉक्टर से सलाह लेना जरूरी है।"
        )

    elif "hemoglobin" in report_text or "wbc" in report_text:
        result_en = (
            "Some blood test values are not within the normal range. "
            "This may be related to low hemoglobin or signs of infection or inflammation. "
            "A healthcare professional can guide you on further tests or treatment."
        )
        result_hi = (
            "कुछ रक्त जांच मान सामान्य नहीं हैं। "
            "यह कम हीमोग्लोबिन या संक्रमण से जुड़ा हो सकता है। "
            "आगे की जांच और सलाह के लिए डॉक्टर से संपर्क करें।"
        )

    else:
        result_en = (
            "The medical report was reviewed and no major abnormalities were detected. "
            "However, regular health checkups are always recommended for overall well-being."
        )
        result_hi = (
            "इस मेडिकल रिपोर्ट में कोई बड़ी असामान्यता नहीं पाई गई है। "
            "फिर भी, अच्छे स्वास्थ्य के लिए नियमित जांच कराते रहना उचित है।"
        )

    # -------- Language selection --------
    final_result = result_hi if language == "hi" else result_en

    return jsonify({"result": final_result})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)



