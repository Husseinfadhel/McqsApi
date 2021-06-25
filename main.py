import uvicorn as uvicorn
from fastapi import FastAPI
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session, conn

app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/grade')
def grade():
    query = session.query(Grade).all()
    print(query)
    return query


@app.post('/grade/add/<stage>')
def grade_add(stage):
    return conn.execute('INSERT INTO Grade (stage) VALUES ({})'.format(stage))


