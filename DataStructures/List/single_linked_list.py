def size(new_list):
    return new_list['size'] #retorno el valor que este en size

def first_element(my_list):
    return my_list['first']['info'] # #me paro en el primer elemento, y luego accedo al valor info y lo retorno

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0: # caso de eliminar el primer nodo de la lista
        my_list['first'] = my_list['first']['next'] #cambiar first para que apunte al nodo consecutivo (2ndo nodo)
        if my_list['size'] = 1: # si unicamente el tamaño de la lista era ese unico nodo (1 nodo), ponemos que el apuntador del ultimo valor es nulo (no existe) por lo tanto la lista no tiene mas nodos.
            my_list['last'] = None
    else:
        ant = my_list['first'] #definimos anterior como el primer nodo de la lista
        for i in range(pos - 1): #Recorro la lista hasta posicion -1 veces (El nodo anterior al que me interesa eliminar)
            ant =ant['next']
        ant['next'] = ant['next']['next']# al estar parado en el que deseo eliminar (ant['next']), ahora lo salto usando next para que mi apuntador señale al siguiente del eliminado. 
        if ant['next'] is None: # Si se borro el ultimo nodo de la lista, se acutaliza al nuevo ultimo last. 
            my_list['last']= ant
            
    my_list['size'] -= 1 #actualizar el tamaño de la lista
    return my_list # y listo =)
    
def change_info(my_list, pos, new_info)
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo = my_list['first'] #inicio nodo en la primera posicion
    for i in range(pos) #recorro hasta pos
        nodo= nodo['next'] 
    nodo['info'] == new_info #actualizo la informacion
    return my_list #retorno

def exchange(my_list, pos_1, pos_2):
    if pos_1 < o or pos_1 >= size(my_list) or if pos_2 < o or pos_2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    nodo1 = my_list['first'] # primera posicion
    for i in range(pos_1): # voy a la posicion n
        nodo1= nodo1['next']
    nodo2 = my_list['first'] 
    for w in range(pos_2):
        nodo2 = nodo2['next']
        
    nodo1['info'], nodo2['info'] == nodo2['info'], nodo1['info'] # intercambio a la vez los dos valores
    return my_list
    
        

        





    


        
    