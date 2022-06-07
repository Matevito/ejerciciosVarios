from functools import reduce

def getPrintResponse(rutineId, total):
    outputText = "La factura {} tiene un total en pesos de {:,.2f}".format(rutineId, total)
    return outputText

def removeElementList(index, list):
    listLength = len(list)
    editedList = []
    for i in range(0, listLength):
        if i != index:
            editedList.append(list[i])
            
    return editedList

def multOrders(value):
    # map function
    quantity = value[1]
    price = value[2]
    return price * quantity
    
def adition (a, b):
    return a + b

def ordenes(rutinaContable):
    print("------------------------ Inicio Registro diario ---------------------------------")
    for rutine in rutinaContable:
        editedList = removeElementList(0, rutine)
        
        toupleListPrices = list(map(multOrders ,editedList))
        reducedPrices = reduce(adition, toupleListPrices)
        # conditional of total fee
        if reducedPrices < 600000:
            reducedPrices += 25000
        
        rutineId = rutine[0]
        outputText = getPrintResponse(rutineId, reducedPrices)
        print(outputText)
    print("-------------------------- Fin Registro diario ----------------------------------")
    

testRutine = [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

ordenes(testRutine)