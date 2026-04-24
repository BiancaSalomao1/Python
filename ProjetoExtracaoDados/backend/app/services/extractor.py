from app.services.nlp_service import extract_entities
from app.services.regex_service import extract_cpf

def extract_data(text: str):
    data = extract_entities(text)

    cpf = extract_cpf(text)
    data["cpf"] = cpf

    return data