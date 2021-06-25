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
    conn.execute('INSERT INTO Grade (stage) VALUES ({})'.format(stage))
    return {'insert': 'Done'}


@app.get('/semesters')
def semesters():
    query = session.query(Semesters).all()
    print(query)
    return query


@app.post('/semesters/add/<seme>')
def grade_add(seme):
    conn.execute('INSERT INTO Semesters (num) VALUES ({})'.format(seme))
    return {'insert': 'Done'}
