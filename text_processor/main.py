__all__ = ()

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextContent(BaseModel):
    content: str


@app.post("/count_words")
async def count_words_endpoint(text: TextContent):
    word_count = len(text.content.split())
    return {"word_count": word_count}