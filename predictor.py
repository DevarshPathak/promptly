from transformers import pipeline
import re


class NextWordPredictor:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="distilgpt2",
            tokenizer="distilgpt2"
        )

    def clean_word(self, word: str) -> str:
        word = word.strip()
        word = re.sub(r"[^a-zA-Z'-]", "", word)
        return word.lower()

    def extract_first_word(self, original_text: str, generated_text: str) -> str:
        new_part = generated_text[len(original_text):].strip()

        if not new_part:
            return ""

        words = new_part.split()

        if not words:
            return ""

        return self.clean_word(words[0])

    def predict(self, text: str, top_k: int = 5):
        text = text.strip()

        if not text:
            return []

        outputs = self.generator(
            text,
            max_new_tokens=3,
            num_return_sequences=top_k * 3,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            temperature=0.7,
            pad_token_id=50256
        )

        predictions = []
        seen = set()

        for output in outputs:
            generated_text = output["generated_text"]
            word = self.extract_first_word(text, generated_text)

            if not word or len(word) < 2:
                continue

            if word not in seen:
                seen.add(word)
                predictions.append({
                    "word": word,
                    "completed_sentence": generated_text
                })

            if len(predictions) >= top_k:
                break

        return predictions
