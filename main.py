def MCD(n1, n2):
    if n2 == 0:
        return n1
    else:
        return MCD(n2, n1 % n2)

def Repeticion(palabra,veces):
    if veces==0:
        return 0
    else:
        return 1+Repeticion(palabra,veces)

def contar_letras(cadena,letra):
    if cadena=="":
        return 0
    if cadena[0]==letra:
        return 1+contar_letras(cadena[1:],letra)
    else:
        return contar_letras(cadena[1:],letra)

def conversion_Binario(n):
    if n/2==0:
        return 0
    else:


def numeros_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + numeros_digitos(n // 10)


while True:
    print("==Menu==")
    print("1. Minimo comun divisor")
    print("2. Repeticion de palabras")
    print("3. Contar Letras en cadena")
    print("4. Convertir a binario")
    print("5. Calcular digitos de un numero")
    print("6. Salir")
    opcion=int(input("Seleccione una opcion"))
    if opcion==1:
        print("---Minimo comun divisor---")
        n1=int(input("Ingrese su primer numero (debe ser numero enteros positivos): "))
        n2=int(input("Ingrese el segundo numero (debe ser numero entero positivo): "))

    elif opcion==2:
        print("---Repeticion de palabras---")
        palabra=input("Ingrese la palabra que sea repetir: ")
        veces=int(input("Ingrese la veces que se repetira la palabra: "))
    elif opcion==3:
        print("---Contar letras---")
        cadena=input("Ingrese la cadena: ")
        letra=input("Ingrese la letra: ")
    elif opcion==4:
        print("---Convertir a Binario---")
        n=int(input("Ingrese un numero para convertir a binario: "))
    elif opcion==5:
        print("---Calcular digitos---")
        n=int(input("Ingrese un numero (entero positivo): "))

    elif opcion==6:
        print("!Hasta pronto¡")
        break
    else:
        print("Opcion no valida vuelva a intentar")