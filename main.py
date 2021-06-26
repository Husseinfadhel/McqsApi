from fastapi import FastAPI
from pydantic import BaseModel
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session

app = FastAPI()

Base.metadata.create_all(engine)


class Grad(BaseModel):
    stage: int


class Sem(BaseModel):
    seme: int
    grade_id: int


class Mo(BaseModel):
    name: str
    grade_id: int
    semester_id: int


class Mcq(BaseModel):
    question: str
    choice_A: str
    choice_B: str
    choice_C: str
    choice_D: str
    answer: str
    module_id: int


class Umo(BaseModel):
    grade_id: int
    semester_id: int
    module_id: int
    module_name: str


class Moc(BaseModel):
    question: str
    choice_A: str
    choice_B: str
    choice_C: str
    choice_D: str
    answer: str
    module_id: int
    mcq_id: int


@app.get('/grade')
def grade():
    query = session.query(Grade).all()
    print(query)
    return 200, {'Response': 'OK', 'Grades': query}


@app.post('/grade/add')
def grade_add(grad: Grad):
    new = Grade(stage=grad.stage)
    Grade.insert(new)
    return 201, {'Response': 'OK'}


@app.get('/semesters')
def semesters():
    query = session.query(Semesters).all()
    print(query)
    return 200, {'Response': 'OK', 'Semesters': query}


@app.post('/semesters/add/')
def grade_add(seme: Sem):
    new = Semesters(num=seme.seme, grade_id=seme.grade_id)
    Semesters.insert(new)
    return 201, {'Response': 'OK'}


@app.get('/Modules')
def mod():
    qu = session.query(Modules).all()
    return 200, {'Response': 'OK', 'Modules': qu}


@app.post("/Module/add")
def modul(model: Mo):
    new = Modules(name=model.name, grade_id=model.grade_id, semester_id=model.semester_id)
    Modules.insert(new)
    return 201, {'Response': 'OK'}


@app.put("/Module/edit")
def upd(umod: Umo):
    n = session.query(Modules).get(umod.module_id)
    n.name = umod.module_name
    n.grade_id = umod.grade_id
    n.semester_id = umod.semester_id
    Modules.update(n)
    return 204, {'Response': 'OK'}


@app.get('/mcqs')
def mcqs():
    quer = session.query(Mcqs).all()
    return 200, {'Response': 'OK', 'Mcqs': quer}


@app.post('/mcqs/add')
def mcq_add(mcq: Mcq):
    new = Mcqs(question=mcq.question, choice_A=mcq.choice_A, choice_B=mcq.choice_B, choice_C=mcq.choice_C,
               choice_D=mcq.choice_D, answer=mcq.answer, module_id=mcq.module_id)
    Mcqs.insert(new)
    return 201, {'Response': 'OK'}


@app.put('/mcqs/edit')
def mcq_edit(edo: Moc):
    mcc = session.query(Mcqs).get(edo.mcq_id)
    mcc.question = edo.question
    mcc.choice_A = edo.choice_A
    mcc.choice_B = edo.choice_B
    mcc.choice_C = edo.choice_C
    mcc.choice_D = edo.choice_D
    mcc.answer = edo.answer
    mcc.module_id = edo.module_id
    Mcqs.update(mcc)
    return 204, {'Response': 'OK'}
