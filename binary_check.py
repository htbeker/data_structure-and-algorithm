def binary_check(items,item):
    if len(items)==0:
        return False
    if item>items[-1]:
        return False
    if item <items[0]:
        return False
    n = len(items)//2
    if item ==items[n]:
        return True
    else:
        if item < item[n]:
            return binary_check(items[:n])
        else:
            return binary_check(items[n:])
