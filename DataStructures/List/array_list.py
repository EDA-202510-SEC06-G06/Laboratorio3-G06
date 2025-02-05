
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
    

        
 
    
    
    
    
    
    
