def get_minimum_item(L):
    L_size = len(L)
    if L_size == 0:
        raise Exception('List is Empty.')
    minimum_item = L[0]
    for i in range(1, L_size):
        if L[i] < minimum_item:
            minimum_item = L[i]
    return minimum_item


def get_maximum_item(L):
    L_size = len(L)
    if L_size == 0:
        raise Exception('List is Empty.')
    maximum_item = L[0]
    for i in range(1, L_size):
        if L[i] > maximum_item:
            maximum_item = L[i]
    return maximum_item


def get_min_max_item(L):
    L_size = len(L)
    if L_size == 0:
        raise Exception('List is Empty.')
    minimum_item = L[0]
    maximum_item = L[0]
    for i in range(1, L_size):
        if L[i] < minimum_item:
            minimum_item = L[i]
        elif L[i] > maximum_item:
            maximum_item = L[i]
    return minimum_item, maximum_item


def counting_sort(L, minimum_item=None, maximum_item=None):
    L_size = len(L)
    if L_size == 0:
        return L
    if not minimum_item or not maximum_item:
        minimum_item, maximum_item = get_min_max_item(L)
    counting_list = [0 for x in range(maximum_item - minimum_item + 1)]
    for i in range(L_size):
        counting_list[L[i] - minimum_item] += 1
    result = list()
    for i in range(len(counting_list)):
        for j in range(counting_list[i]):
            result += [i + minimum_item]
    return result


def insertion_sort(L):
    L_size = len(L)
    if L_size == 0:
        return L
    for i in range(1, L_size):
        tmp = L[i]
        x = i
        while x > 0 and L[x - 1] > tmp:
            L[x] = L[x - 1]
            x -= 1
        L[x] = tmp
    return L


def bubble_sort(L):
    L_size = len(L)
    if L_size == 0:
        return L
    for i in range(L_size):
        swapped = False
        for j in range(L_size - 1):
            if L[j + 1] < L[j]:
                L[j + 1], L[j] = L[j], L[j + 1]
                swapped = True
        print(L)
        if not swapped:
            break
    return L


def selection_sort(L):
    L_size = len(L)
    if L_size == 0:
        return L
    for i in range(L_size):
        min_item = i
        for j in range(i + 1, L_size):
            if L[j] < L[min_item]:
                min_item = j
        if i != min_item:
            L[i], L[min_item] = L[min_item], L[i]
    return L


def merge_sort(L):
    if len(L) < 2:
        return L
    L1 = L[:len(L) // 2]
    L2 = L[len(L) // 2:]
    L1 = merge_sort(L1)
    L2 = merge_sort(L2)

    i = j = 0
    L = []

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L += [L1[i]]
            i += 1
        else:
            L += [L2[j]]
            j += 1
    L += L1[i:] + L2[j:]
    return L