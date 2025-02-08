def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False
    
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    if is_empty(my_list):
        node= {"info": element, "next": None}
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        node= {"info": element, "next": my_list["first"]}
        my_list["first"] = node
        my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    if is_empty(my_list):
        node= {"info": element, "next": None}
        my_list["first"] = node
        my_list["size"] += 1
        my_list["last"] = node
    else:
        node= {"info": element, "next": None}
        my_list["size"] += 1
        my_list["last"] = node
    return my_list

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        return my_list["last"]["info"]
    
