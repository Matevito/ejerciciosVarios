def removeInTouple(index, touple):
    # remover elemento de lista de tuplas segun indice dado
    editedTouple = []
    for element in touple:
        if(element == touple[index]):
            continue
        else:
            editedTouple.append(element)
    return tuple(editedTouple)

def getOutputText(registro , id):
    # crear string para imrpimir en consola
    text = "Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}".format(id, 
                                                                                                                                            registro[0],
                                                                                                                                            registro[1],
                                                                                                                                            registro[2],
                                                                                                                                            registro[3],
                                                                                                                                            registro[4],
                                                                                                                                            registro[5],
                                                                                                                                            registro[6])
    return text

def AutoPartes(ventas: list): 
    '''
    input: ventas as a touple list* 
    output: dictionary with touple list*
    '''
    editedVentas = {}
    for touple in ventas: 
        # revisar existencias en editedVentas
        key = str(touple[0])
        if key not in editedVentas:
            editedVentas[key] = []
        editedToupleList = removeInTouple(0, touple)
        editedVentas[key].append(editedToupleList)
        
    return editedVentas

def consultaRegistro(ventas, idProducto):
    # 2. check if id is on ventas list;
    key = str(idProducto)
    if (key in ventas):
        for register in ventas[key]:
            printResponse = getOutputText(register, idProducto)
            print(printResponse)
    else:
        print("No hay registro de venta de ese producto")
