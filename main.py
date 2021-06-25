import uvicorn as uvicorn
from fastapi import FastAPI
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session

app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/grade')
def grade():
    query = session.query(Grade).all()
    print(query)
    return query


@app.post('/grade/add/<stage>')
def grade_add(stage):
    grade_create = Grade(stage=Grade.stage)
    Grade.insert(grade_create)
    session.commit()
    session.close()
    return Grade.insert(grade_create)

