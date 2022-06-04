def removeInTouple(index, touple):
    # remover elemento de lista de tuplas segun indice dado
    editedTouple = []
    for element in touple:
        if(element == touple[index]):
            continue
        else:
            editedTouple.append(element)
    return tuple(editedTouple)

def outputText(ventas, idProducto):
    pass

def AutoPartes(ventas: list): 
    '''
    input: ventas as a touple list* 
    output: dictionary with touple list*
    '''
    editedVentas = {}
    
    for touple in ventas: 
        # revisar existencias en editedVentas
        if editedVentas.get(touple[0]) == None:
            '''
            Crear un diccionario para el registro es tan tonto por este condicional...
            '''
            editedVentas[touple[0]] = []
        editedToupleList = removeInTouple(0, touple)
        editedVentas[touple[0]].append(editedToupleList)
        
    return editedVentas

def consultaRegistro(ventas, idProducto):
    # 1. crear diccionario de tuplas
    # reduce list of touples to list of ids
    registroVentas = AutoPartes(ventas)

    # 2. check if id is on ventas list;
    if idProducto in registroVentas:
        pass
    else:
        print("No hay registro de venta de ese producto")

prubaVentas = [(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]

print(consultaRegistro(prubaVentas,  2001));