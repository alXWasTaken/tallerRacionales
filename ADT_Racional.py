import math
import sys

sys.setrecursionlimit(10000)

class Racional():
    
    #Constructor
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    #Suma
    def __add__(self, racional):
        numerador = (self.numerador * racional.denominador) + (self.denominador * racional.numerador)
        denominador = self.denominador * racional.denominador
        mcd = math.gcd(numerador,denominador)
        return Racional(numerador//mcd, denominador//mcd)
        
    #Resta
    def __sub__(self, racional):
        numerador = (self.numerador * racional.denominador) - (self.denominador * racional.numerador)
        denominador = self.denominador * racional.denominador
        mcd = math.gcd(numerador,denominador)
        return Racional(numerador//mcd, denominador//mcd)

    #Multiplicación
    def __mul__(self, racional):
        numerador = self.numerador * racional.numerador
        denominador = self.denominador * racional.denominador
        mcd = math.gcd(numerador,denominador)
        return Racional(numerador//mcd, denominador//mcd)

    #División
    def __truediv__(self,racional):
        numerador = self.numerador * racional.denominador
        denominador = self.denominador * racional.numerador
        mcd = math.gcd(numerador,denominador)
        return Racional(numerador//mcd, denominador//mcd)

    #Potenciación
    def __pow__(self, exp):
        numerador = self.numerador ** exp
        denominador = self.denominador ** exp
        return Racional(numerador, denominador)
    
    #Menor que
    def __lt__(self, racional):
        num1 = self.numerador/self.denominador
        num2 = racional.numerador/racional.denominador
        if (num1 < num2):
            return Racional(self.numerador, self.denominador)
        else:
            return Racional(racional.numerador, racional.denominador)
        
    #Mayor que
    def __gt__(self, racional):
        num1 = self.numerador/self.denominador
        num2 = racional.numerador/racional.denominador
        if (num1 < num2):
            return Racional(racional.numerador, racional.denominador)
        else:
            return Racional(self.numerador, self.denominador)

    #Equals
    def __eq__(self, racional):
        if(self.numerador == racional.numerador and self.denominador == racional.denominador):
            return True
        else:
            return False

    #Escritura
    def __str__(self):
        return str(self.numerador) + '/' + str(self.denominador)



r1 = Racional(1,2) 
r2 = Racional(1,4)

#Suma de racionales
r3 = r1+r2

print('Suma de racionales: ')
print(r3)

#Resta de racionales

r3 = r1-r2

print('Resta de racionales: ')
print(r3)


#Multiplicación de racionales:
r3 = r1*r2

print('Multiplicación de racionales: ')
print(r3)     

#División de racionales: 

r3 = r1/r2

print('División de racionales: ')
print(r3) 

#Potenciación de racionales 

r3 = r1**2

print('Potenciación de racionales: ')
print(r3) 

#Menor que

r3 = r1 < r2

print('Menor que: ')
print(r3) 

#Mayor que

r3 = r1 > r2

print('Mayor que: ')
print(r3) 

#Equals

if(r1==r2):
    print('Son iguales')
else:
    print('No son iguales')


#Pruebas Unitarias

assert( r1+r2 == Racional(3,4))
assert( r1-r2 == Racional(1,4))
assert( r1*r2 == Racional(1,8))
assert( r1/r2 == Racional(2,1))
assert( r1**2 == Racional(1,4))

print('Después de pruebas unitarias: ')
print('Ok')

string = "1/2 1/4 + 1/5 / 7/3 *"

def opFunt(self):
    operadores = ["+" ,"-" ,"/" ,"*" ,"^" ,">" ,"<"]
    racionales =[]
    operandos = []
    racionales = self.split()
    elim =[]
    for x in range(0, len(racionales)) :
        if racionales[x] in operadores :
            operandos.append(racionales[x])
    for y in range(0, len(racionales)) : 
        if racionales[y] in operandos :
            elim.append(y)
    for z in range(0, len(elim)) :
        print(racionales[elim[z]])
    return racionales, operandos


print(opFunt(string))