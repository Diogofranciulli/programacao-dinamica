def busca(lista, alvo):
    if len(lista) == 0:
        return False
    else:
        if lista[0] == alvo:
            return True
        else:
            lista.pop(0)
            return busca(lista, alvo)

lista = [1,2,3,4,5,6]

print(busca(lista, 4))