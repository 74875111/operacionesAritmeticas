def inputNumbers():
    numero1=float(input("Ingrese numero 1: "))
    numero2=float(input("Ingrese numero 2: "))
    return numero1,numero2
def suma(a,b):
    return a+b


if __name__=="__main__":
    a, b = inputNumbers()
    print(f"{a}+{b}={suma(a,b)}")

