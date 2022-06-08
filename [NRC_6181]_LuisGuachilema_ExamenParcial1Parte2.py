class Calculo:
    '''
    Clase calculo que contiene los metodos de suma, factorial y multiplicacion
    Tiene como parametros los numeros que se ingresan por el usuario
    '''
    def __init__(self, numeroIngresado1, numeroIngresado2):
        self.numero1 = numeroIngresado1
        self.numero2 = numeroIngresado2
    def MetodoFactorial(self):
        '''
        Metodo que calcula el factorial de un numero que obtiene  numero 1 ingreso por usuario
        '''
        factorial = 1
        for i in range(1, self.numero1 + 1):
            factorial = factorial * i
            print("Factorial de", i, "es:", factorial)
        return factorial
    def MetodoSuma(self):
        '''
        Método que suma dos numeros que obtiene  numero 2 ingreso por usuario
        '''
        suma = 0
        for i in range(1, self.numero2 + 1):
            suma = suma + i
            print("Suma de :", str(i),"+",suma,"=", suma)
        return suma
    def testPrimo(self):
        '''
        Método para determinar si un numero es primo o no, en este paso usaremos el numero 2 ingresado por el usuario
        '''
        for i in range(2, self.numero2 + 1):
            if self.numero2 % i == 0:
                print("El numero", self.numero2, "no es primo")
                break
        else:
            print("El numero", self.numero2, "es primo")
    def tableMult(self):
        for i in range(1, 11 ):
            print(self.numero1, "x", i, "=", self.numero1 * i)
datosIngresado=Calculo(int(input("Ingrese el primer número")), int(input("Ingrese el segundo número:")))
print("----------------------------------------------------")
print("          Método Factorial de la clase Calculo")
print("----------------------------------------------------")
print(Calculo.MetodoFactorial(datosIngresado))
#print(Calculo().MetodoFactorial())
print("----------------------------------------------------")
print("      Método Suma N números de la clase Calculo")
print("----------------------------------------------------")
print(Calculo.MetodoSuma(datosIngresado))
print("----------------------------------------------------")
print("          Método testPrimo de la clase Calculo")
print("----------------------------------------------------")
print(Calculo.testPrimo(datosIngresado))
print(Calculo().testPrimo())
print("----------------------------------------------------")
print("          Método testPrimo de la clase Calculo")
print("----------------------------------------------------")
