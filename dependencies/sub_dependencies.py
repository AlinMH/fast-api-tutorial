from typing import Optional

import uvicorn
from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


if __name__ == '__main__':
    uvicorn.run('sub_dependencies:app', host='127.0.0.1', log_level='info', reload=True)
