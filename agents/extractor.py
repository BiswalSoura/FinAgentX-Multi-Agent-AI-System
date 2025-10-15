import re
def extract_financials(text: str):
    out={}
    m = re.search(r'(revenue[^0-9\$]*\$?([0-9\.,]+)\s*(billion|million|bn|m)?)', text, re.I)
    if m: out['revenue_raw'] = m.group(1)
    m2 = re.search(r'eps[^0-9\-]*([-+]?[0-9]*\.?[0-9]+)', text, re.I)
    if m2: out['EPS'] = m2.group(1)
    out['mentions_beat'] = bool(re.search(r'\bbeat(s|ing)?\b', text, re.I))
    out['mentions_miss'] = bool(re.search(r'\bmiss(ed)?\b', text, re.I))
    return out
