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
    text = "Producto consultado : {} Descripción {} #Parte {} Cantidad vendida {} Stock {} Comprador {} Documento {} Fecha Venta {}".format(id, 
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
        if editedVentas.get(touple[0]) == None:
            editedVentas[touple[0]] = []
        editedToupleList = removeInTouple(0, touple)
        editedVentas[touple[0]].append(editedToupleList)
        
    return editedVentas

def consultaRegistro(ventas, idProducto):
    # 1. crear diccionario de tuplas
    # reduce list of touples to list of ids
    registroVentas = AutoPartes(ventas)

    # 2. check if id is on ventas list;
    if (idProducto in registroVentas):
        for register in registroVentas[idProducto]:
            printResponse = getOutputText(register, idProducto)
            print(printResponse)
    else:
        print("No hay registro de venta de ese producto")

prubaVentas =[(5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
(3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
(3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
(8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]

consultaRegistro(prubaVentas,  2010)