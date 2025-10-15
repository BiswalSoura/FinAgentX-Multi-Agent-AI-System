def analyze(extracted, text):
    note=""
    conclusion="neutral"
    if 'EPS' in extracted:
        try:
            eps = float(extracted['EPS'])
            note += f"EPS reported: {eps}. "
        except:
            note += f"EPS reported: {extracted.get('EPS')}. "
    if extracted.get('mentions_beat'):
        conclusion = 'bullish'
        note += "Text indicates company beat estimates. "
    if extracted.get('mentions_miss'):
        conclusion = 'bearish'
        note += "Text indicates company missed estimates. "
    return {'note':note,'conclusion':conclusion}
