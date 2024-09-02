class OperacionAritmeticas():
    def inputNumbers(self):
        numero1=float(input("Ingrese numero 1: "))
        numero2=float(input("Ingrese numero 2: "))
        return numero1,numero2
    def suma(self,a,b):
        return a+b


if __name__=="__main__":
    operacion=OperacionAritmeticas()
    a, b = operacion.inputNumbers()
    print(f"{a}+{b}={operacion.suma(a,b)}")
