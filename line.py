def line():
    print("TO DO")
    import math

    coefA = float(input("Ingrese el coeficiente A: "))
    coefB = float(input("Ingrese el coeficiente B: "))
    coefX1 = float(input("Ingrese el coeficiente X1: "))
    coefX2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {(coefA)}")
    print(f"El coeficiente B de su ecuación de la recta es: {(coefB)}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {(coefX1)}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {(coefX2)}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefA}X + {coefB}")
    x1 = coefA * coefX1 + coefB
    x2 = coefA * coefX2 + coefB
    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coefX1}, {x1})")
    print(f"\tP2 ({coefX2}, {x2})")
    print("")
    print(f"La distancia entre ellos es: {math.dist((coefX1, x1), (coefX2, x2))}")
