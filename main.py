from fastapi import FastAPI
import uvicorn
from app.routers import show, comment, rating

app = FastAPI()
app.include_router(show.router)
app.include_router(comment.router)
app.include_router(rating.router)


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)