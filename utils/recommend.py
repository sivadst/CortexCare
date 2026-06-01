def recommend(data):
    tips = []

    if data["sleep_hours"] < 6:
        tips.append("Sleep at least 7 hours tonight")

    if data["screen_time"] > 6:
        tips.append("Reduce screen time before bed")

    if data["peer_pressure"] > 7:
        tips.append("Take breaks from stressful environments")

    return tips