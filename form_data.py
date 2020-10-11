import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


if __name__ == '__main__':
    uvicorn.run('form_data:app', host='127.0.0.1', log_level='info', reload=True)
