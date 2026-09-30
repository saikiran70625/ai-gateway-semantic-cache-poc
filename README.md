# AI Gateway – Semantic Cache POC

A Proof of Concept demonstrating how an AI Gateway can reduce unnecessary Large Language Model (LLM) API calls using semantic caching.

## Problem

Every user request sent directly to an LLM can consume tokens, compute resources, money, and processing time.

Many users ask questions that are identical or very similar to questions that have already been answered.

For example:

* "What is Retrieval Augmented Generation?"
* "Can you explain RAG?"

Although the wording is different, both questions have a very similar meaning.

Calling the LLM again for the second question may be unnecessary.

## Solution

This POC introduces a lightweight AI Gateway between the user and the LLM.

The gateway:

1. Receives the user's question.
2. Generates an embedding for the question.
3. Searches previously answered questions.
4. Calculates semantic similarity.
5. Returns a cached answer when a sufficiently similar question exists.
6. Calls the LLM only when no suitable cached answer exists.
7. Stores the new response for future requests.

## Architecture

```text
                User
                  |
                  v
             AI Gateway
                  |
                  v
          Generate Embedding
                  |
                  v
          Semantic Cache
             /       \
          HIT         MISS
           |            |
           v            v
     Cached Answer      LLM
                        |
                        v
                  Save Response
```

## Example

### First request

```text
User:
What is Retrieval Augmented Generation?

Gateway:
Cache MISS

        ↓

LLM is called

        ↓

Answer is generated

        ↓

Answer is stored in cache
```

### Similar request

```text
User:
Can you explain RAG?

Gateway:
Cache HIT

        ↓

Return cached answer

        ↓

No LLM call
```

## Key Technologies

* Python
* FastAPI
* OpenAI Embeddings
* OpenAI LLM
* NumPy
* Semantic Similarity

## Why Semantic Caching?

Traditional caching compares the exact request.

For example:

```text
"What is RAG?"
```

and

```text
"Explain RAG"
```

would be treated as different requests.

Semantic caching compares the meaning of the requests using embeddings.

This allows the gateway to identify similar questions even when the wording is different.

## Potential Benefits

### Cost Reduction

Avoid unnecessary LLM calls and reduce token consumption.

### Performance

Cached responses can be returned much faster than generating a new response.

### Scalability

Frequently asked questions can be served without repeatedly consuming LLM resources.

### Green AI

Reducing unnecessary model inference can also reduce compute consumption.

## Current POC Limitation

The current implementation uses an in-memory cache.

This means cached data is lost when the application restarts.

For a production implementation, the cache could be replaced with:

* Redis
* Qdrant
* ChromaDB
* PostgreSQL with vector search

Additional capabilities can also be added:

* Cache expiration
* Model routing
* Prompt optimization
* Token tracking
* Cost monitoring
* Cache analytics

## Future Architecture

```text
                         User
                           |
                           v
                     AI Gateway
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Semantic       Prompt        Intelligent
         Cache       Optimizer        Router
             |             |             |
             +-------------+-------------+
                           |
                           v
                    Selected LLM
                           |
                           v
                       Response
```

## Future Improvements

1. Add Redis-based distributed caching.
2. Add cache expiration and invalidation.
3. Add intelligent model routing.
4. Add prompt optimization.
5. Add token and cost tracking.
6. Add monitoring dashboard.
7. Measure actual cost and latency savings.

## Learning Outcome

This project demonstrates the basic architecture of an AI Gateway and how semantic caching can be used to optimize LLM applications.
