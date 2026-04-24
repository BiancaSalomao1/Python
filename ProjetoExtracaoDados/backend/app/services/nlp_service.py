import spacy

nlp = spacy.load("pt_core_news_sm")

def extract_entities(text: str):
    doc = nlp(text)

    entities = {
        "nome": None,
        "data": None,
        "valor": None
    }

    for ent in doc.ents:
        if ent.label_ == "PER" and not entities["nome"]:
            entities["nome"] = ent.text

        if ent.label_ == "DATE" and not entities["data"]:
            entities["data"] = ent.text

        if ent.label_ == "MONEY" and not entities["valor"]:
            entities["valor"] = ent.text

    return entities