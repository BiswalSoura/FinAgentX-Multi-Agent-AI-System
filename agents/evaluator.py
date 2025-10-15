def evaluate(processed):
    score = 0.0
    if processed.get('extracted'): score += 0.4
    if processed.get('summary_short') and processed.get('specialist'): score += 0.35
    short = processed.get('summary_short','')
    if 10 < len(short) < 400: score += 0.25
    feedback = "OK" if score >= 0.7 else "Needs improvement: add market reaction or concrete figures"
    return {'score': round(score,2), 'feedback': feedback}
