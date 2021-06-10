import uvicorn as uvicorn
from fastapi import FastAPI
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session
from fastapi.encoders import jsonable_encoder

app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/')
def root():
    query = session.query(Grade).all()
    print(query)
    return query
