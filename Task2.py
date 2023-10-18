## Задание 2

cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
fn = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]


def zipLists(country, fnx):
    dictcountry = dict(zip(country, fnx))
    print(dictcountry)


zipLists(cnt, fn)