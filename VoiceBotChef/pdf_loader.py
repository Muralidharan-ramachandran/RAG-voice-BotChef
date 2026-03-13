import fitz

def load_recipes(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    recipes = text.split("~ ~  - * -  ~ ~")
    return recipes