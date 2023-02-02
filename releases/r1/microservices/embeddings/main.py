import logging
import time
from random import random
from typing import Callable, List

import tensorflow_hub as hub
import uvicorn
from fastapi import Body, FastAPI, Request
from pydantic import BaseModel


class EmbeddingsRequest(BaseModel):
    strings: List[str]


class EmbeddingsResponse(EmbeddingsRequest):
    embeddings: List[float]


log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    """All responses come with process time information"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/", response_model=EmbeddingsResponse)
async def embed(
    payload: EmbeddingsRequest = Body(
        ..., example={"strings": ["test 1", "test 2", "foo", "bar"]}
    )
) -> EmbeddingsResponse:
    """Embeds a list of strings, returning a list of floats for every string input"""
    # embeddings = [i.numpy().tolist() for i in EMBED(payload.strings)]
    embeddings = [random() for _ in range(len(payload.strings))]
    return EmbeddingsResponse(embeddings=embeddings, **payload.dict())


if __name__ == "__main__":
    # USEv5 is about 100x faster than 4
    EMBED = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
    uvicorn.run("main:app", host="0.0.0.0", port=8088, reload=True)
