from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from models import Items
from sqlmodel import Field, Session, SQLModel, create_engine

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/Items/{1}")
# def read_Item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/save")
def save_item(item: Items):
    item1 = Items(name=item.name, model=item.model, controller=item.controller,  number=item.number)
    with Session(engine) as session:
        session.add(item1)
        session.commit()

@app.get("/all")
async def get_all_sessions():
    json_sessions = []
    with Session(engine) as session:
        sessions = session.exec(select(QSession)) 
        json_sessions = [{"username": s.user_id, "filename": s.filename, "duration": s.duration, "machine_id": s.machine_id} for s in sessions]

    print(json_sessions)
    return json_sessions