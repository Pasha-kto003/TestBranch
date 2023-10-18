## Задание 3
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
list1 = []
list2 = []


def calcPairs(pair):
    for i in pairs:
        list1.append(i)
        list2.append(int(i[0] * i[1]))
        calc = dict(zip(list1, list2))
    print(calc)


calcPairs(pairs)