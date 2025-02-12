def new_list():
    
    array = {"size": 0, "elements" :[]}
    
    return array
   
    
def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list,  element, cmp_function):
    
    size = my_list["size"]
    
    if size > 0:
        
        keyexist = False
        
        for keypos in range(0, size):
            
            info = my_list["elements"][keypos]
            
            if cmp_function(element, info) == 0:
                
                keyexist = True
                
                break 
            
        if keyexist:
            
            return keypos

    return -1


def add_first(my_list, element):
    
    my_list["elements"].insert(0, element)
    
    my_list["size"] += 1
    
    return my_list


def add_last(my_list, element):
    
    my_list["elements"].append(element)
    
    my_list["size"] += 1
    
    return my_list


def size(my_list):
    
    return my_list["size"]


def first_element(my_list):
    
    if size(my_list) == 0:
        
        return "IndexError: list index out of range"
    
    else:
        
        return my_list["elements"][size(my_list) - 1]
    

def is_empty(my_list):
    
    if my_list["size"] == 0:
        
        return True
    
    else:
        
        return  False
      

def remove_first(my_list):
    
    if is_empty(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["size"] -= 1
        return my_list["elements"].pop(0)
    

def remove_last(my_list):
    
    if is_empty(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["size"] -= 1
        return my_list["elements"].pop(my_list["size"])
    
    
def insert_element(my_list, element, pos):
    
    my_list["elements"].insert(pos, element)
    
    return my_list


def sub_list(my_list, pos_i, num_elements):
    
    if my_list["size"] < pos_i:
        
        return "IndexError: list index out of range"
    
    else:
        #Esta debería ser la manera correcta, Sí pide una lista 
        """"
        new_list = my_list["elements"][pos_i : (pos_i + num_elements)]
        return new_list
        """
        
        #Si lo que realemnte pide es una lista hecha (dict) sería así:
        #Y de hecho esto es lo que funciona
        my_list["elements"] = my_list["elements"][pos_i : (pos_i + num_elements)]
        my_list["size"] = num_elements
        return my_list
    

def delete_element(my_list, pos):
    
    if not 0 <= pos < size(my_list):
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list
    

def change_info(my_list, pos, new_info):
    
    if my_list["size"] < pos:
        
        return "IndexError: list index out of range"
    
    else:
        
        my_list["elements"][pos] = new_info
        return my_list
    

def exchange(my_list, pos_1, pos_2):
    
    if my_list["size"] < pos_2 or my_list["size"] < pos_1:
        
        return "IndexError: list index out of range"
    
    else:
        
        temp = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = temp
        return my_list