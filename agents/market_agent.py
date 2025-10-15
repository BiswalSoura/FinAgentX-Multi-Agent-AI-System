def analyze(text):
    macros=[]
    t = (text or "").lower()
    if 'inflation' in t: macros.append('inflation')
    if 'unemployment' in t: macros.append('unemployment')
    context = f"Macro themes detected: {', '.join(macros)}"
    return {'note':context, 'conclusion': 'macro_note'}
