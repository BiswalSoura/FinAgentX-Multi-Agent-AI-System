def summarize(title, text, extracted):
    short = f"{title} — "
    if 'revenue_raw' in extracted:
        short += f"{extracted['revenue_raw']}. "
    elif 'EPS' in extracted:
        short += f"EPS: {extracted['EPS']}. "
    else:
        short += "Key figures not found. "
    sentiment = 'neutral'
    if extracted.get('mentions_beat'): sentiment = 'bullish'
    if extracted.get('mentions_miss'): sentiment = 'bearish'
    short += f"Sentiment: {sentiment}."
    long = short + " Full analysis: " + (text[:800] + '...')
    return {'short':short,'long':long,'sentiment':sentiment}
