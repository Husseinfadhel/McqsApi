from fastapi import FastAPI, Depends, Security
from pydantic import *
from models import McqModel, McqModelUpdate, client, collection, GetModule
from fastapi_auth0 import Auth0, Auth0User
from typing import *

app = FastAPI()

auth = Auth0(domain='bmcapi.jp.auth0.com', api_audience='bmcapi.jp-auth0.com',
             scopes={'read:users': 'create & edit mcqs'})


@app.get('/mcq/{gd:int}/{smester:int}/{module:str}/', response_description="List Mcqs", response_model=list[McqModel])
async def mcq_list(gd, smester, module):
    mcq = collection.find({"Grade": gd, "Semesters": smester, "Modules": module})
    list_mcq = list(mcq)
    print(list_mcq)
    return list_mcq


@app.get('/Modules', response_model=GetModule)
def mod(mo: GetModule):
    modules = collection.find({"Grade": mo.Grade, "Semesters": mo.Semester, "Modules": mo.Module})
    list_m = list(modules)
    modules = []
    for doc in list_m:
        module = doc['Modules']
        modules.append({"Module": module})

    return modules


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
