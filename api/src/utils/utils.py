import re

def process_prompt_utils(prompt: str) -> str:
    # define regex pattern to remove all text between square brackets and parentheses
    pattern = r'\[[^\]]*\]|\("[^"]*"\)'
    cleaned_prompt = re.sub(pattern, '', prompt)
    return cleaned_prompt
