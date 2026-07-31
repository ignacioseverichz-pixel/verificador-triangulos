print("=" * 40)
print("      VERIFICADOR DE TRIANGULOS")
print("=" * 40)

try:
    lado_a = float(input("INGRESE EL LADO A DEL TRIANGULO: "))
    lado_b = float(input("INGRESE EL LADO B DEL TRIANGULO: "))
    lado_c = float(input("INGRESE EL LADO C DEL TRIANGULO: "))

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        print("ERROR: LOS LADOS DEBEN SER MAYORES QUE CERO.")

    elif (
        lado_a + lado_b <= lado_c
        or lado_a + lado_c <= lado_b
        or lado_b + lado_c <= lado_a
    ):
        print("LOS VALORES INGRESADOS NO FORMAN UN TRIANGULO.")

    elif lado_a == lado_b == lado_c:
        print("EL TRIANGULO ES EQUILATERO.")

    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("EL TRIANGULO ES ISOSCELES.")

    else:
        print("EL TRIANGULO ES ESCALENO.")

except ValueError:
    print("ERROR: DEBE INGRESAR VALORES NUMERICOS.")
