import pymongo
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
    mcq = collection.find({"Grade": gd, "Semesters": smester, "Modules": module}).sort("_id", pymongo.ASCENDING)
    list_mcq = list(mcq)
    print(list_mcq)
    return list_mcq


@app.get('/Modules/{gd:int}/{sem:int}')
def mod(gd, sem):
    modules = collection.find({"Grade": gd, "Semesters": sem})
    list_m = list(modules)
    modules = []
    for doc in list_m:
        module = doc['Modules']
        modules.append({"Module": module})

    return modules
