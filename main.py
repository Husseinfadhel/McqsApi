from fastapi import FastAPI
from pydantic import BaseModel
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session, conn

app = FastAPI()

Base.metadata.create_all(engine)


class Grad(BaseModel):
    stage: int


class Semes(BaseModel):
    seme: int
    grade_id: int

@app.get('/grade')
def grade():
    query = session.query(Grade).all()
    print(query)
    return query


@app.post('/grade/add')
def grade_add(grad: Grad):
    new = Grade(stage=grad.stage)
    Grade.insert(new)
    return {'insert': 'Done'}


@app.get('/semesters')
def semesters():
    query = session.query(Semesters).all()
    print(query)
    return query


@app.post('/semesters/add/')
def grade_add(seme: Semes):
    new = Semesters(num=seme.seme, grade_id=seme.grade_id)
    Semesters.insert(new)
    return {'insert': 'Done'}
