import json
from \
    core.fakerFunc \
import \
    funcName, \
    funcNameF, \
    funcNameM, \
    funcCPF, \
    funcDateB

def getNome(amount: int = 1, sex: str = "I"):
    listReturn = []
    for i in range(amount):
        listReturn.append(funcName(False, sex))
    return listReturn

def getPai(amount: int = 1):
    listReturn = []
    for i in range(amount):
        listReturn.append(funcNameF(False))
    return listReturn

def getMae(amount: int = 1):
    listReturn = []
    for i in range(amount):
        listReturn.append(funcNameM(False))
    return listReturn

def getCpf(amount: int = 1, mask: bool = False):
    listReturn = []
    for i in range(amount):
        listReturn.append(funcCPF(False, mask))
    return listReturn

def getDtnasci(
    minAge: int = 0,
    maxAge : int = 115,
    amount: int = 1,
    mask: str = "%Y-%m-%d"
):
    listReturn = []
    for i in range(amount):
        listReturn.append(funcDateB(False, minAge, maxAge, mask))
    return listReturn

def getPessoa(
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
            listItem.append('{' + funcName(True))
            listItem.append(funcNameM(True))
            listItem.append(funcNameF(True))
            listItem.append(funcCPF(True, maskCPF))
            listItem.append(funcDateB(True, minAge, maxAge, maskDt) + '}')
            try:
                listReturn.append(json.loads(','.join(listItem)))
                vLoop = False
            except:
                vLoop = True
            
    return listReturn