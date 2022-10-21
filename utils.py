from googletrans import Translator


def translate(phrase: str, dest_lang: str) -> str:
    translator = Translator()
    return translator.translate(phrase, dest=dest_lang).text