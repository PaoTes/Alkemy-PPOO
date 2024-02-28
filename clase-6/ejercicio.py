"""
Enunciado
Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""

class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso

    def mostrar_datos(self):
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Año de Ingreso: {self.anioIngreso}")


class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, sueldoBasico, porcentajeAdicional):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.sueldoBasico = sueldoBasico
        self.porcentajeAdicional = porcentajeAdicional

    def mostrar_salario(self):
        antiguedad = 2024 - self.anioIngreso
        aumento = 0
        if antiguedad >= 5:
            aumento = 0.1
        elif antiguedad >= 2:
            aumento = 0.05
        salario = self.sueldoBasico * (1 + aumento)
        print(f"Salario: ${salario}")


class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, salarioMinimo, clientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente

    def mostrar_salario(self):
        salario = self.clientesCaptados * self.montoPorCliente
        if salario < self.salarioMinimo:
            salario = self.salarioMinimo
        print(f"Salario: ${salario}")


def empleado_con_mas_clientes(empleados):
    mayor_clientes = 0
    empleado_con_mas_clientes = None
    for empleado in empleados:
        if isinstance(empleado, EmpleadoComision):
            if empleado.clientesCaptados > mayor_clientes:
                mayor_clientes = empleado.clientesCaptados
                empleado_con_mas_clientes = empleado
    return empleado_con_mas_clientes


# Crear empleados fijos
empleado1 = EmpleadoFijo(500, "Pedro", "Martínez", 2022, 15000, 0.05)
empleado2 = EmpleadoFijo(500, "Juan", "Pérez", 2020, 10000, 0.05)
empleado3 = EmpleadoFijo(500, "María", "Gómez", 2018, 12000, 0.1)
empleado4 = EmpleadoFijo(500, "Paola", "Testa", 2022, 15000, 0.05)
empleado5 = EmpleadoFijo(500, "Lorena", "Crespo", 2021, 13000, 0.05)

# Crear empleados a comisión
empleado6 = EmpleadoComision(250, "Laura", "Díaz", 2021, 10000, 50, 20)
empleado7 = EmpleadoComision(250, "Roberto", "Suárez", 2020, 12000, 20, 40)
empleado8 = EmpleadoComision(250, "Camila", "Rojas", 2020, 15000, 5, 100)
empleado9 = EmpleadoComision(250, "Mario", "Santa", 2023, 15000, 5, 100)
empleado10 = EmpleadoComision(250, "Alejandra", "Minguez", 2020, 15000, 5, 100)


# Lista de empleados
empleados = [empleado1, empleado2, empleado3, empleado4, empleado5, empleado6, empleado7, empleado8, empleado9, empleado10]

# Mostrar datos de los empleados
for empleado in empleados:
    empleado.mostrar_datos()
    empleado.mostrar_salario()

# Mostrar el empleado con más clientes
empleado_con_mas_clientes = empleado_con_mas_clientes(empleados)
if empleado_con_mas_clientes is not None:
    print(f"\nEl empleado con más clientes es: {empleado_con_mas_clientes.nombre} {empleado_con_mas_clientes.apellido}")
else:
    print("No hay empleados a comisión")
