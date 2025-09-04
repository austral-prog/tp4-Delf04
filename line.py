def line():
    import math

    coefA = float(input("Ingrese el coeficiente A: "))
    coefB = float(input("Ingrese el coeficiente B: "))
    coefX1 = float(input("Ingrese el coeficiente X1: "))
    coefX2 = float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {(coefA)}")
    print(f"El coeficiente B de su ecuación de la recta es: {(coefB)}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {(coefX1)}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {(coefX2)}")

    print("\nPara la siguiente ecuación:")
    print(f"	Y = {coefA}X + {coefB}")
    x1 = coefA * coefX1 + coefB
    x2 = coefA * coefX2 + coefB
    print("\nDados los siguientes puntos:")
    print(f"	P1 ({coefX1}, {x1})")
    print(f"	P2 ({coefX2}, {x2})")

    print(f"\nLa distancia entre ellos es: {math.dist((coefX1, x1), (coefX2, x2))}")
