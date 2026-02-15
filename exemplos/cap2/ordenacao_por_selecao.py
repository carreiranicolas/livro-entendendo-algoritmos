def buscaMenor(arr):
    menor = arr[0]
    indice_menor = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indice_menor = i
    
    return indice_menor


def ordenacaoporSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        indice_menor = buscaMenor(arr)

        novoArr.append(arr.pop(indice_menor))
    
    return novoArr


print(ordenacaoporSelecao([5, 3, 6, 2, 10]))