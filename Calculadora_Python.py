# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:17:55 2022

@author: david
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:25:02 2021
@author: DavidAlcázarSánchez
"""

#Calculadora 
#Suma de 2 números
#Resta de dos números
#Multiplicación de dos números
#División de dos números
#Módulo entre dos números
#Cociente entre dos números
#Exponente de un número elevado a otro
#Calculadora de áreas de círculos para 'n' números pares simultáneos
#Calculadora de áreas de círculos para 'n' números pares simultáneos
#Salir
#Introduce una opción

Calculadora = int(input("¡Hola! Soy tu calculadora. Introduzca el número asignado a la operación que quieras realizar.\n \
Las opciones son:\n \
1. Suma de dos números.\n \
2. Resta de dos números.\n \
3. Multiplicación de dos números.\n \
4. División de dos números.\n \
10. Salir. \n \
Introduce el número para la operación que quieras realizar: "))

if Calculadora == 1:
    Num1 = float(input("Has elegido el modo suma de dos números. Elige el primer número (puede tener dos decimales): "))
    Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la suma de {Num1} y {Num2} es {Num1 + Num2}")

elif Calculadora == 2:
    Num1 = float(input("Has elegido el modo resta de dos números. Elige el primer número (puede tener dos cifras decimales): "))
    Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la resta de {Num1} y {Num2} es {Num1 - Num2}")

elif Calculadora == 3:
    Num1 = float(input("Has elegido el modo multiplicación de dos números. Elige el primer número (puede tener dos cifras decimales): "))
    Num2 = float(input("Elige el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la multiplicación de {Num1} por {Num2} es {Num1 * Num2}")

elif Calculadora == 4:
    Num1 = float(input("Has elegido el modo división de dos números. Elige el primer número (puede tener dos cifras decimales): "))
    Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    while Num2 == 0:
        print ("¡El divisor no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la división de {Num1} entre {Num2} es {Num1 / Num2}")



elif Calculadora == 10:
    print ("Has seleccionado la opción salir. ¡Hasta luego!")

else:
    print ("¡No tenemos ninguna operación asignada a ese número!") 