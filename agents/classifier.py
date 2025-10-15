def classify(text: str):
    t = (text or "").lower()
    if any(w in t for w in ['eps','earnings','quarter','q1','q2','q3','q4']):
        return {'type':'earnings','confidence':0.9}
    if any(w in t for w in ['fed','inflation','unemployment','gdp','rates']):
        return {'type':'macro','confidence':0.85}
    return {'type':'news','confidence':0.7}
