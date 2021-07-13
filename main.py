from fastapi import FastAPI, Depends, Security
from pydantic import BaseModel
from models import Grade, Semesters, Modules, Mcqs, Base, engine, session
from fastapi_auth0 import Auth0, Auth0User

app = FastAPI()
Base.metadata.create_all(engine)

auth = Auth0(domain='bmcapi.jp.auth0.com', api_audience='bmcapi.jp-auth0.com',
             scopes={'read:users': 'create & edit mcqs'})


class Grad(BaseModel):
    stage: int
    id: int


class Sem(BaseModel):
    seme: int
    grade_id: int
    id: int


class Mo(BaseModel):
    name: str
    grade_id: int
    semester_id: int
    id: int


class Mcq(BaseModel):
    question: str
    choice_A: str
    choice_B: str
    choice_C: str
    choice_D: str
    answer: str
    module_id: int


class Mcqd(BaseModel):
    id: int


class Umo(BaseModel):
    grade_id: int
    semester_id: int
    module_id: int
    module_name: str


class Dmo(BaseModel):
    id: int


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


@app.post('/grade/add', dependencies=[Depends(auth.implicit_scheme)])
def grade_add(grad: Grad, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    new = Grade(stage=grad.stage)
    Grade.insert(new)
    return 201, {'Response': 'OK', 'User': user}


@app.delete('/grade/delete')
def gd_delete(grad: Grad, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    session.query(Grade).filter_by(id=grad.id).delete()
    session.commit()
    return 205, {'Response': 'OK'}


@app.get('/semesters')
def semesters():
    query = session.query(Semesters).all()
    print(query)
    return 200, {'Response': 'OK', 'Semesters': query}


@app.post('/semesters/add/', dependencies=[Depends(auth.implicit_scheme)])
def grade_add(seme: Sem, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    new = Semesters(num=seme.seme, grade_id=seme.grade_id)
    Semesters.insert(new)
    return 201, {'Response': 'OK'}


@app.delete('/semesters/delete/', dependencies=[Depends(auth.implicit_scheme)])
def sem_delete(seme: Sem, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    session.query(Semesters).filter_by(id=seme.id).delete()
    session.commit()
    return 205, {'Response': 'OK'}


@app.get('/Modules')
def mod():
    qu = session.query(Modules).all()
    return 200, {'Response': 'OK', 'Modules': qu}


@app.post("/Module/add", dependencies=[Depends(auth.implicit_scheme)])
def modul(model: Mo, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    new = Modules(name=model.name, grade_id=model.grade_id, semester_id=model.semester_id)
    Modules.insert(new)
    return 201, {'Response': 'OK'}


@app.put("/Module/edit", dependencies=[Depends(auth.implicit_scheme)])
def upd(umod: Umo, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    n = session.query(Modules).get(umod.module_id)
    n.name = umod.module_name
    n.grade_id = umod.grade_id
    n.semester_id = umod.semester_id
    Modules.update(n)
    return 204, {'Response': 'OK'}


@app.delete("/Module/delete/", dependencies=[Depends(auth.implicit_scheme)])
def mod_del(mode: Dmo, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    session.query(Modules).filter_by(id=mode.id).delete()
    session.commit()
    return 204, {'Response': 'OK'}


@app.get('/mcqs/')
def mcqs():
    quer = session.query(Mcqs).all()
    return 200, {'Response': 'OK', 'Mcqs': quer}


@app.post('/mcqs/add', dependencies=[Depends(auth.implicit_scheme)])
def mcq_add(mcq: Mcq, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    new = Mcqs(question=mcq.question, choice_A=mcq.choice_A, choice_B=mcq.choice_B, choice_C=mcq.choice_C,
               choice_D=mcq.choice_D, answer=mcq.answer, module_id=mcq.module_id)
    Mcqs.insert(new)
    return 201, {'Response': 'OK'}


@app.put('/mcqs/edit', dependencies=[Depends(auth.implicit_scheme)])
def mcq_edit(edo: Moc, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
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


@app.delete('/mcq/delete', dependencies=[Depends(auth.implicit_scheme)])
def mcq_dele(mcq: Mcqd, user: Auth0User = Security(auth.get_user), scopes=['read:users']):
    session.query(Mcqs).filter_by(id=mcq.id).delete()
    session.commit()
    return 204, {'Response': 'OK'}
