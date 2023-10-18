## Задание 4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5, 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2, 'Ursula': 4, 'Viktor': 5}
for i, j in grades.items():
    print(f"Оценка {j} у {i}")

excel = []
for i, j in grades.items():
    if j == 5:
        excel.append(i)
print(excel)

good = []
for i, j in grades.items():
    if j == 4:
        good.append(i)
print(good)

satisf = []
for i, j in grades.items():
    if j == 3:
        satisf.append(i)
print(satisf)

bad = []
for i, j in grades.items():
    if j == 2:
        bad.append(i)
print(bad)