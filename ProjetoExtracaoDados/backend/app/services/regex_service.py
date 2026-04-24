import re

def extract_cpf(text: str):
    match = re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}', text)
    return match.group() if match else None