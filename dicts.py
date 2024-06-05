def create_inventory(items):
    my_dict = dict()
    for i in range(len(items)):
        if items[i] in my_dict:
            my_dict[items[i]] += 1
        else:
            my_dict[items[i]] = 1
    return my_dict

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    my_dict = dict()
    dict_items = create_inventory(items)
    valueIn = list(inventory.values())
    valueIt = list(dict_items.values())
    valueTot = []

    for i in range(len(valueIn)):
        x = valueIn[i] - valueIt[i]
        if x > 0:
            valueTot.append(x)
        else:
            valueTot.append(0)

    keyTot = list(inventory.keys())
    index = 0
    while(index < len(keyTot)):
        key = keyTot[index]
        value = valueTot[index]
        my_dict[key] = value
        index += 1
    return my_dict

def remove_item(inventory, item):
    found = False
    for key in inventory.keys():
        if key == item:
            found = True 
            break
        else:
            found = False
    if found == True:
        del inventory[item]
        return inventory
    else:
        return inventory

def list_inventory(inventory):
    for key, value in inventory.items():
        if value == 0:
            found = True 
            break
        else:
            found = False
    if found == True:
        del inventory[key]
        return list(inventory.items())
    else:
        return list(inventory.items())
