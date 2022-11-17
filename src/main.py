from fastapi import FastAPI
from faker import Faker

app = FastAPI()
fake = Faker('pt_BR')

@app.get("/nome")
def nome():
    return {'nome: ' + fake.name().replace(".","")}

@app.get("/CPF")
def cpf():
    return {'CPF: ' + fake.cpf().replace(".","").replace("-","")}

@app.get("/data")
def data(minimum_age: int = 0, maximum_age : int = 115):
    return {'Data: ' + fake.date_of_birth(None, minimum_age, maximum_age).strftime("%Y-%m-%d")}

@app.get("/pessoa")
def pessoa(minimum_age: int = 0, maximum_age : int = 115):
    return {
        '{"nome": ' + fake.name().replace(".","") + chr(13) +
        ',"mae": ' + fake.name_female().replace(".","") + chr(13) +
        ',"pai": ' + fake.name_male().replace(".","") + chr(13) +
        ',"CPF": ' + fake.cpf().replace(".","").replace("-","") + chr(13) +
        ',"dtNasci": ' + fake.date_of_birth(None, minimum_age, maximum_age).strftime("%Y-%m-%d") + '}'
    }