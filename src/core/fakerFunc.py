from faker import Faker

fake = Faker('pt_BR')

def funcName(dblQuotes: bool = True, sex: str = "I"):
    if (sex == "F"):
        name = fake.name_female()
    elif(sex == "M"):
        name = fake.name_male()
    else:
        name = fake.name()

    if dblQuotes:
        return '"nome": "' + name.replace(".","") + '"'
    else:
        return 'nome: ' + name.replace(".","")

def funcNameM(dblQuotes: bool = True):
    if dblQuotes:
        return '"mae": "' + fake.name_female().replace(".","") + '"'
    else:
        return 'mae: ' + fake.name_female().replace(".","")

def funcNameF(dblQuotes: bool = True):
    if dblQuotes:
        return '"pai": "' + fake.name_male().replace(".","") + '"'
    else:
        return 'pai: ' + fake.name_male().replace(".","")

def funcCPF(dblQuotes: bool = True, mask: bool = False):
    if mask:
        doc = fake.cpf()
    else:
        doc = fake.cpf().replace(".","").replace("-","")
    if dblQuotes:
        return '"CPF": ' + doc
    else:
        return 'CPF: ' + doc

def funcDateB(
    dblQuotes: bool = True,
    minAge: int = 0,
    maxAge : int = 115,
    mask: str = "%Y-%m-%d"
):
    if dblQuotes:
        return '"dtNasci": "' + fake.date_of_birth(None, minAge, maxAge).strftime(mask) + '"'
    else:
        return 'dtNasci: ' + fake.date_of_birth(None, minAge, maxAge).strftime(mask)