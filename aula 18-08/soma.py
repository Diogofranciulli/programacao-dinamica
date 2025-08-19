def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])

lista = [1,2,3,4,5,6,7,8,9,10]

print(soma(lista))