__all__ = ()

from .tasks import count_words


class TextValidator:
    def validate_content(self, content):
        if not content or len(content.strip()) < 10:
            raise ValueError("Content must be at least 10 characters long")

        return True


class TextProcessor:
    def __init__(self, text_id):
        self.text_id = text_id

    def process_async(self):
        count_words.delay(self.text_id)