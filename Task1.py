## Задание 1

rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха"}


def changeRept(rpt):
    rept["snake"] = "змея"
    rept["tortoise"] = rept.pop("tortoize")
    print(rept)
    for i, j in rpt.items():
        print(f"{i.capitalize()} : {j}")


changeRept(rept)


def printRept(rpt):
    for i, j in rpt.items():
        print(f"{j.capitalize()} по английски будет {i}")


printRept(rept)