"""Crear una clase llamada Animal, otra llamada Perro y otra llamada
Águila.
↪ La clase Animal tiene:
○ atributo cantidad_patas: numérico
○ atributo tipo: vertebrado/invertebrado
○ método comer(): retorna un string “estoy comiendo”
↪ La clase Perro hereda de Animal y agrega:
○ atributo nombre: texto
○ atributo raza: texto
○ método correr(): retorna un string “estoy corriendo”
↪ La clase Aguila hereda de Animal y agrega:
○ método volar(): retorna un string “estoy volando”"""
import inspect

from enum import Enum

class TipoAnimal(Enum):
    VERTEBRADO = "vertebrado"
    INVERTEBRADO = "invertebrado"

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo
    def comer(self):
        return "Estoy comiendo"
    
class Perro(Animal):
    def __init__(self, nombre, raza, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)
        self.nombre=nombre
        self.raza=raza
    def correr(self):
        return "Estoy corriendo"
    
class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)
        
    def volar(self):
        return "Estoy volando"
    

    
perro1 = Perro("Coli", "Caniche", 4, TipoAnimal.VERTEBRADO)
nombre_clase = perro1.__class__.__name__
print (f"Hola!! mi nombre es {perro1.nombre}, soy un {nombre_clase}, de raza {perro1.raza}, soy {(TipoAnimal.VERTEBRADO.value).lower()}, tengo {perro1.cantidad_patas} patas y {(perro1.comer()).lower()} !!" )

aguila1 = Aguila( 2, TipoAnimal.VERTEBRADO)
nombre_clase = aguila1.__class__.__name__
print (f"Hola!! soy un {nombre_clase}, soy  {(TipoAnimal.VERTEBRADO.value).lower()}, tengo {aguila1.cantidad_patas} patas y {(aguila1.volar()).lower()} !!" )