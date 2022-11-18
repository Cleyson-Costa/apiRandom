from \
    fastapi \
import \
    FastAPI
from \
    fastapi.responses \
import \
    JSONResponse
from \
    auxMain \
import \
    getNome, \
    getPai, \
    getMae, \
    getCpf, \
    getDtnasci, \
    getPessoa

app = FastAPI()

@app.get("/nome")
def nome(amount: int = 1, sex: str = "I"):
    return JSONResponse(getNome(amount, sex))

@app.get("/pai")
def pai(amount: int = 1):
    return JSONResponse(getPai(amount))

@app.get("/mae")
def mae(amount: int = 1):
    return JSONResponse(getMae(amount))

@app.get("/CPF")
def cpf(amount: int = 1, mask: bool = False):
    return JSONResponse(getCpf(amount, mask))

@app.get("/dtnasci")
def dtnasci(
    minAge: int = 0,
    maxAge : int = 115,
    amount: int = 1,
    mask: str = "%Y-%m-%d"
):
    return JSONResponse(getDtnasci(minAge, maxAge, amount, mask))

@app.get("/pessoa")
def pessoa(
    minAge: int = 0,
    maxAge: int = 115,
    amount: int = 1,
    maskCPF: bool = False,
    maskDt: str = "%Y-%m-%d"
):
    return JSONResponse(getPessoa(minAge, maxAge, amount, maskCPF, maskDt))