
def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"La suma de los números {num1} y {num2} es:", resultado)

def resta():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"La diferencia entre de los números {num1} y {num2} es:", resultado)

def multiplicacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El producto de los números {num1} y {num2} es:", resultado)

def division():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"La división de {num1} y {num2} es:", resultado)

def main():
    while True:
        print("Opciones:")
        print("1. Sumar.")
        print("2. Restar ")
        print("3. Multiplicación ")
        print("4. División ")
        print("5. Salir del programa.")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplicacion()
        elif opcion == "4":
            division()
        elif opcion == "5":
            print("¡Fin del Programa!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 , 3 ,4  ó 5")

if __name__ == "__main__":
    main()
