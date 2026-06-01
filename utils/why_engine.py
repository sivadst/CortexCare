def generate_reason(data):
    reasons = []

    if data["sleep_hours"] < 6:
        reasons.append("Low sleep is increasing your stress")

    if data["screen_time"] > 6:
        reasons.append("High screen time is affecting mental state")

    if data["peer_pressure"] > 7:
        reasons.append("Peer pressure is a major stress driver")

    return reasons