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
        x = i - 1
        while x >= 0 and tmp < L[x]:
            L[x + 1] = L[x]
            x -= 1
            
    return L


print(insertion_sort([8,4,9,2,3,4,7]))