def analyze_haemoglobin(haemoglobin):

    results = []
    if haemoglobin < 11:
        results.append({
            "disease": "Anemia",
            "probability": 88,
            "reason": (
                "Haemoglobin level is lower than"
                " normal healthy range."
            ),
            "remedy": (
                "Increase iron-rich foods like "
                "spinach, beetroot, and dates.")})
    if haemoglobin<10:
        results.append({"disease":"Fatigue Syndrome",
            "probability":74,
            "reason": (
                "Low haemoglobin may reduce "
                "oxygen transportation."),"remedy": ("Take proper rest and improve "
                "daily nutrition.")})
    if haemoglobin<9:
        results.append({"disease": "Malnutrition","probability": 68,"reason": (
                "Very low haemoglobin may indicate "
                "nutritional deficiency."),
            "remedy": ("Maintain balanced diet and "
                "consult a physician.")})
    return results
