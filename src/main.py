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
        'nome: ' + fake.name().replace(".","") +
        ',mae: ' + fake.name_female().replace(".","") +
        ',pai: ' + fake.name_male().replace(".","") +
        ',CPF: ' + fake.cpf().replace(".","").replace("-","") +
        ',dtNasci: ' + fake.date_of_birth(None, minimum_age, maximum_age).strftime("%Y-%m-%d") + '}'
    }