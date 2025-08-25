def conta(lista,item):
    if len(lista) == 0:
        return 0
    elif lista[0] == item:
        lista.pop(0)
        return 1 +conta(lista, item)
    else:
        lista.pop(0)
        return 0 +conta(lista, item)