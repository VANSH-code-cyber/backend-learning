from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------
# Data Model
# -------------------
class User(BaseModel):
    id: int
    name: str
    age: int

# -------------------
# Routes
# -------------------
@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/users")
def create_user(user: User):
    return {
        "status": "user created",
        "user": user
    }