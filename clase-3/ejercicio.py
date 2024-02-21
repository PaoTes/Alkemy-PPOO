def accion_a():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("La suma de los números es:", resultado)

def accion_b():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print("El producto de los números es:", resultado)

def main():
    while True:
        print("Opciones:")
        print("1. Sumar dos números.")
        print("2. Multiplicar dos números.")
        print("3. Salir del programa.")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            accion_a()
        elif opcion == "2":
            accion_b()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()