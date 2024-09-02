from operacionesAritmeticas import OperacionAritmeticas
if __name__=="__main__":
    operacion=OperacionAritmeticas()
    a, b = operacion.inputNumbers()
    print(f"{a}+{b}={operacion.suma(a,b)}")