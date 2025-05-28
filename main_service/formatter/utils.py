__all__ = ()

from .tasks import count_words


def update_word_count(text):
    count_words.delay(text.id)
