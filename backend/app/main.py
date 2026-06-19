from fastapi import FastAPI

from app.database import engine
from app.database import Base

from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ReBill API")


@app.get("/")
def home():
    return {
        "message": "ReBill API Running"
    }