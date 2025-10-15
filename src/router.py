def route(processed):
    typ = processed.get('type','news')
    if typ == 'earnings':
        return 'earnings'
    if typ == 'macro':
        return 'market'
    return 'news'
