import random
from time import time


def bubble_sort(arranjo):
    # bubble sort
    n = len(arranjo)
    for i in range(n):  # quantidade de iteraÃ§Ãµes
        for j in range(n - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                arranjo[j], arranjo[j + 1] = arranjo[j + 1], arranjo[j]


def insertion_sort(arranjo):
    for i in range(1, len(arranjo)):
        chave = arranjo[i]
        j = i
        while j > 0 and arranjo[j - 1] > chave:
            arranjo[j] = arranjo[j - 1]
            j -= 1
        arranjo[j] = chave


def selection_sort(arranjo):
    for i in range(len(arranjo)):
        min_index = i
        for j in range(i + 1, len(arranjo)):
            if arranjo[j] < arranjo[min_index]:
                min_index = j
        if min_index != i:
            arranjo[i], arranjo[min_index] = arranjo[min_index], arranjo[i]


def merge_sort(arranjo):
    if len(arranjo) > 1:
        mid = len(arranjo) // 2
        left = arranjo[0:mid]
        right = arranjo[mid:]

        # Chamada recursiva em cada metade
        merge_sort(left)
        merge_sort(right)

        # a partir daqui vamos fazer o "merge" das sublistas
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arranjo[k] = left[i]
                i += 1
            else:
                arranjo[k] = right[j]
                j += 1
            k += 1

        # valores restantes
        while i < len(left):
            arranjo[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arranjo[k] = right[j]
            j += 1
            k += 1
        
        return arranjo


# Verifica se x estÃ¡ presente em arranjo, retornando
# (True, Ã­ndice). Se x nÃ£o estiver, retorna (False, -1)
def binary_search(arranjo, x):
    '''
    Verifica se x  estÃ¡ presente em arranjo (arranjo precisa estar ordenado)
    :param arranjo: lista ordenada de valores
    :param x: valor a ser procurado na lista
    :return: True e o Ã­ndice da lista onde x se encontra, False e -1, caso contrÃ¡rio
    '''
    low = 0
    high = len(arranjo) - 1
    # Enquanto o arranjo nÃ£o tiver sido percorrido por completo
    while low <= high:
        # encontra o meio do arranjo
        mid = (high + low) // 2
        # se o valor foi maior que o valor que estÃ¡ no meio do arranjo
        # ignora toda a parte anterior ao meio do arranjo
        if arranjo[mid] < x:
            low = mid + 1
        # se o valor for menor, faz o contrÃ¡rio
        elif arranjo[mid] > x:
            high = mid - 1
        # caso contrÃ¡rio, o elemento estÃ¡ exatamente no meio
        else:
            return True, mid
    # elemento nÃ£o estÃ¡ no arranjo
    return False, None


def binary_search_recursive(arranjo, low, high, x):
    # Caso base
    if high >= low:
        mid = (high + low) // 2
        # testa se valor estÃ¡ no centro do arranjo
        if arranjo[mid] == x:
            return True, mid

        # se x for menor, estÃ¡ do lado direito do arranjo
        elif arranjo[mid] > x:
            return binary_search_recursive(arranjo, low, mid - 1, x)

        # caso contrÃ¡rio (x maior), valor estÃ¡ do lado esquerdo
        else:
            return binary_search_recursive(arranjo, mid + 1, high, x)
    else:
        # NÃ£o estÃ¡ presente no arranjo
        return False, -1


def maior_lista(l):
    if len(l) == 1:
        return l[0]
    else:
        m = maior_lista(l[1:])
        return m if m > l[0] else l[0]


def maior_lista2(l, m):
    if len(l) <= 1:
        return m
    else:
        if l[0] > m:
            return maior_lista2(l[1:], l[0])
        else:
            return maior_lista2(l[1:], m)


if __name__ == '__main__':
    l = [6, 5, 3]
    selection_sort(l)
    print(l)

    myList = [6, 5, 3, 7, -1]  # , 31, 44, 55, 20]
    print(maior_lista(myList))

    merge_sort(myList)
    print(myList)

    binary_search_recursive([1, 2, 4, 20, 51], 0, 4, 51)

    """a = [random.randint(0, 50000) for i in range(10000)]
    b = [random.randint(0, 50000) for i in range(1000000)]

    start = time()
    sort_1(a) # O(n^2)
    #print(a)
    end = time()
    print(end - start)

    start = time()
    sort_2(b) # O(log n)
    #print(b)
    end = time()
    print(end - start)
    """