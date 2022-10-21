from unittest import TestCase
from googletrans import Translator


def translate(phrase: str,
              dest_lang: str) -> str:
    translator = Translator()
    return translator.translate(phrase, dest=dest_lang).text


class TestTranlsator(TestCase):
    def test_one_lower(self):
        word = "мир"
        language = "en"
        self.assertEqual(translate(word, language), "world")

    def test_one_upper(self):
        word = "МИР"
        language = "en"
        self.assertEqual(translate(word, language), "WORLD")

    def test_empty_str(self):
        word = ""
        language = "en"
        self.assertEqual(translate(word, language), "")

    def test_random_letters(self):
        word = "вфывфы"
        language = "en"
        self.assertEqual(translate(word, language), "wfywfy")


if __name__ == "__main__":
    a = TestTranlsator
