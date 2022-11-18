import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import func

app = FastAPI()

@app.get("/nome")
def nome(amount: int = 1, sex: str = "I"):
    listReturn = []
    for i in range(amount):
        listReturn.append(func.getName(False, sex))
    return JSONResponse(listReturn)

@app.get("/pai")
def pai(amount: int = 1):
    listReturn = []
    for i in range(amount):
        listReturn.append(func.getNameF(False))
    return JSONResponse(listReturn)

@app.get("/mae")
def mae(amount: int = 1):
    listReturn = []
    for i in range(amount):
        listReturn.append(func.getNameM(False))
    return JSONResponse(listReturn)

@app.get("/CPF")
def cpf(amount: int = 1, mask: bool = False):
    listReturn = []
    for i in range(amount):
        listReturn.append(func.getCPF(False, mask))
    return JSONResponse(listReturn)

@app.get("/dtnasci")
def dtnasci(
    minAge: int = 0,
    maxAge : int = 115,
    amount: int = 1,
    mask: str = "%Y-%m-%d"
):
    listReturn = []
    for i in range(amount):
        listReturn.append(func.getDateB(False, minAge, maxAge, mask))
    return JSONResponse(listReturn)

@app.get("/pessoa")
def pessoa(
    minAge: int = 0,
    maxAge: int = 115,
    amount: int = 1,
    maskCPF: bool = False,
    maskDt: str = "%Y-%m-%d"
):
    vLoop = True
    while vLoop:
        listReturn = []
        for i in range(amount):
            listItem = []
            listItem.append('{' + func.getName(True))
            listItem.append(func.getNameM(True))
            listItem.append(func.getNameF(True))
            listItem.append(func.getCPF(True, maskCPF))
            listItem.append(func.getDateB(True, minAge, maxAge, maskDt) + '}')
            try:
                listReturn.append(json.loads(','.join(listItem)))
                vLoop = False
            except:
                vLoop = True
            
    return JSONResponse(listReturn)