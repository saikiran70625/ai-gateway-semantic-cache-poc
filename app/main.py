from fastapi import FastAPI
from pydantic import BaseModel

from app.embeddings import generate_embedding
from app.semantic_cache import (
    find_similar_answer,
    save_to_cache
)
from app.llm import ask_llm


app = FastAPI(
    title="AI Gateway - Semantic Cache POC"
)


class ChatRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "AI Gateway Semantic Cache POC"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    query = request.query

    # Generate embedding
    query_embedding = generate_embedding(query)

    # Search semantic cache
    cached_item, similarity = find_similar_answer(
        query_embedding
    )

    # Cache HIT
    if cached_item:

        return {
            "response": cached_item["answer"],
            "source": "semantic_cache",
            "cache_hit": True,
            "similarity": round(similarity, 3)
        }

    # Cache MISS
    answer = ask_llm(query)

    # Save response
    save_to_cache(
        query,
        query_embedding,
        answer
    )

    return {
        "response": answer,
        "source": "llm",
        "cache_hit": False,
        "similarity": round(similarity, 3)
    }
