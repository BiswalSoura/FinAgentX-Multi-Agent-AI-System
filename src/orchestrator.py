from agents.classifier import classify
from agents.extractor import extract_financials
from agents.summarizer import summarize
import json, os
from src.router import route
from agents.evaluator import evaluate
from agents.optimizer import refine

def process_article(article: dict):
    title = article.get('title','No title')
    text = article.get('content') or article.get('description') or ''
    cls = classify(text)
    extracted = extract_financials(text)
    summ = summarize(title, text, extracted)
    return {
        'title': title,
        'type': cls['type'],
        'confidence': cls['confidence'],
        'extracted': extracted,
        'summary_short': summ['short'],
        'summary_long': summ['long'],
        'sentiment': summ['sentiment']
    }

def run_articles(articles, save_memory=True, memory_file=None):
    results=[]
    for a in articles:
        from src.orchestrator import process_article  # uses function defined earlier
        p = process_article(a)
        # route
        r = route(p)
        if r == 'earnings':
            from agents.earnings_agent import analyze as earnings_analyze
            p['specialist'] = earnings_analyze(p.get('extracted',{}), p.get('summary_long',''))
        elif r == 'market':
            from agents.market_agent import analyze as market_analyze
            p['specialist'] = market_analyze(p.get('summary_long',''))
        else:
            p['specialist'] = {'note':'general news','conclusion':'info'}
        # evaluate
        ev = evaluate(p)
        p['evaluation'] = ev
        # optimize if needed
        if ev['score'] < 0.7:
            p = refine(p, ev['feedback'])
            p['evaluation']['post_refine'] = evaluate(p)
        results.append(p)

    # save outputs and memory
    repo_root = r"D:\University of San Diego\Natural Language processing and GenAI\FinAgentX Multi Agent AI System\FinAgentX-Multi-Agent-AI-System"
    out_dir = os.path.join(repo_root, "data","sample","out")
    os.makedirs(out_dir, exist_ok=True)
    outpath = os.path.join(out_dir, "analysis_end2end.json")
    with open(outpath,"w",encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    if save_memory:
        mem_dir = os.path.join(repo_root,"data","memory")
        os.makedirs(mem_dir, exist_ok=True)
        memory_file = memory_file or os.path.join(mem_dir,"memory.json")
        with open(memory_file,"w",encoding="utf-8") as f:
            json.dump({'runs': results}, f, ensure_ascii=False, indent=2)
    print("Saved end-to-end results to", outpath)
    return results
