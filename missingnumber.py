def missing(list1):
    return [i for x, y in zip(list1, list1[1:])
        for i in range(x + 1, y) if y - x > 1]

list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12]
print(missing(list1))




