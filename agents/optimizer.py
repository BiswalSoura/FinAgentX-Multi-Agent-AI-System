def refine(processed, feedback):
    processed['summary_long'] = processed.get('summary_long','') + "\n\nRefinement: " + feedback
    processed['summary_short'] = processed.get('summary_short','') + " | Refinement: " + feedback
    return processed
