import re

def process_pormpt(prompt: str) -> str:
    # define regex pattern to remove all text between square brackets and parentheses
    pattern = r'\[[^\]]*\]|\("[^"]*"\)'
    cleaned_prompt = re.sub(pattern, '', prompt)
    return cleaned_prompt
