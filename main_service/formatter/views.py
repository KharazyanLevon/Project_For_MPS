__all__ = ()

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Text
from .forms import TextForm
import requests


def is_admin(user):
    return user.is_staff


@login_required
def index(request):
    texts = Text.objects.filter(author=request.user)
    return render(request, 'formatter/index.html', {'texts': texts})


@login_required
def delete_text(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    if request.user.is_staff or text.author == request.user:
        text.delete()

    return redirect('index')


def text_list_api(request):
    texts = Text.objects.all().values('id', 'title', 'content', 'word_count')
    return JsonResponse({'texts': list(texts)})

@login_required
def create_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.author = request.user
            text.save()
            
            try:
                response = requests.post('http://localhost:8001/count_words', json={'content': text.content}, timeout=10)
                word_count = response.json().get('word_count', 0)
                text.word_count = word_count
                text.save()
            except Exception:
                text.word_count = 0
                text.save()
            
            return redirect('index')
    else:
        form = TextForm()

    return render(request, 'formatter/create.html', {'form': form})

@login_required
def edit_text(request, text_id):
    text = get_object_or_404(Text, pk=text_id, author=request.user)
    if request.method == 'POST':
        form = TextForm(request.POST, instance=text)
        if form.is_valid():
            text = form.save()
            
            try:
                response = requests.post('http://localhost:8001/count_words', json={'content': text.content}, timeout=10)
                word_count = response.json().get('word_count', 0)
                text.word_count = word_count
                text.save()
            except Exception:
                text.word_count = 0
                text.save()
            
            return redirect('index')
    else:
        form = TextForm(instance=text)

    return render(request, 'formatter/edit.html', {'form': form})