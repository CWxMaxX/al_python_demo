def even(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result


def odd(lst):
    result = []
    for x in lst:
        if x % 2 == 1:
            result.append(x)
    return result
