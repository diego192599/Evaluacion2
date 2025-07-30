def MCD(n1, n2):
    if n2 == 0:
        return n1
    else:
        return MCD(n2, n1 % n2)

def Repeticion(palabra, veces):
    if veces == 0:
        return ""
    else:
        return palabra + Repeticion(palabra, veces - 1)

def contar_letras(cadena,letra):
    if cadena=="":
        return 0
    if cadena[0]==letra:
        return 1+contar_letras(cadena[1:],letra)
    else:
        return contar_letras(cadena[1:],letra)

def conversion_Binario(n):
    if n == 0:
        return ""
    else:
        return conversion_Binario(n // 2) + str(n % 2)

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
    opcion=int(input("Seleccione una opcion: "))
    if opcion==1:
        print("---Minimo comun divisor---")
        n1=int(input("Ingrese su primer numero (debe ser numero enteros positivos): "))
        n2=int(input("Ingrese el segundo numero (debe ser numero entero positivo): "))
        resultado= MCD(n1,n2)
        print(f"EL minimo comun divisor de los numeros de {n1} y {n2} es: {resultado} ")

    elif opcion==2:
        print("---Repeticion de palabras---")
        palabra=input("Ingrese la palabra que sea repetir: ")
        veces=int(input("Ingrese la veces que se repetira la palabra: "))

    elif opcion==3:
        print("---Contar letras---")
        cadena=input("Ingrese la cadena: ")
        letra=input("Ingrese la letra: ")
        resultado=contar_letras(cadena,letra)
        print(f"La palabra {cadena} tiene la cantidad de letra {letra} es: {resultado} ")

    elif opcion==4:
        print("---Convertir a Binario---")
        n=int(input("Ingrese un numero para convertir a binario: "))
        resultado2=conversion_Binario(n)
        print(f"El numero {n} su conversion a binario es {resultado2}")

    elif opcion==5:
        print("---Calcular digitos---")
        n=int(input("Ingrese un numero (entero positivo): "))
        resultado1=numeros_digitos(n)
        print(f"El numero {n} tiene un total de {resultado1} de numeros digitos")

    elif opcion==6:
        print("!Hasta pronto¡")
        break
    else:
        print("Opcion no valida vuelva a intentar")