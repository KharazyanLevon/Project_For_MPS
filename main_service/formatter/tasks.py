__all__ = ()

from celery import shared_task
import requests


@shared_task
def count_words(text_id):
    from .models import Text
    text = Text.objects.get(id=text_id)
    response = requests.post('http://fastapi:8001/count_words', json={'content': text.content})
    if response.status_code == 200:
        word_count = response.json().get('word_count', 0)
        text.word_count = word_count
        text.save()
        
