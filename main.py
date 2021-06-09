from fastapi import FastAPI
from models import Grade, Semesters, Modules, Mcqs, Base, engine, Session

app = FastAPI()

Base.metadata.create_all(engine)


@app.route('/grade')
def grade():
    return Grade.format()
