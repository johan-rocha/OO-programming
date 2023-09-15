#!/usr/bin/env python3

from math import *
    

class Ponto():
    def __init__(self, x_point, y_point):
        self.__x = x_point
        self.__y = y_point
    def show_coordinates(self):
        print(f'coordinate point = ({self.__x},{self.__y})')
    def distancia_deste_ponto(self, other_x, other_y) -> float:
         return abs(sqrt(((other_x - self.__x)**2) + ((other_y - self.__y)**2)))

class Reta(Ponto):
     def __init__(self, ):
          pass
         

class Retangulo():
    def __init__(self, base_init, altura_init):
        self.__base = base_init
        self.__altura = altura_init

    def get_base(self) -> int: 
        return self.__base
    
    def get_altura(self) -> int:
        return self.__altura

    def get_area(self) -> int:
        return self.__base * self.__altura
    
    def get_perimetro(self) -> int:
        return 2 * self.__base + 2 * self.__altura
    
    def eh_quadrado(self) -> bool:
        if(self.__base == self.__altura):
            return True
        else:
            return False

class Triangulo():
    def __init__(self, lado_a_input, lado_b_input, lado_c_input):
        self.__lado_a = lado_a_input
        self.__lado_b = lado_b_input
        self.__lado_c = lado_c_input
    # Formula de Heron
    def get_area(self) -> int:
        semiperimetro = (self.__lado_a + self.__lado_b + self.__lado_c)/2

        area = sqrt(semiperimetro * (semiperimetro - self.__lado_a) * (semiperimetro - self.__lado_b) * (semiperimetro - self.__lado_c))
    
    def get_altura_relativa(self, lado_base) -> int:
        return self.get_area()/lado_base
    
    def get_perimetro(self) -> int:
        return self.__lado_a + self.__lado_b + self.__lado_c
    
    #pela lei dos cossenos
    def mostrar_tipo(self): 
        soma_dos_quadrados = self.__lado_b * self.__lado_b + self.__lado_c * self.__lado_c

        if(self.__lado_a == soma_dos_quadrados):
                print("Trigulo Retângulo\n")
        elif(self.__lado_a < soma_dos_quadrados):
                print("Triangulo acutângulo\n")
        elif(self.__lado_a > soma_dos_quadrados):
                print("Triangulo obstusângulo\n")
        elif(self.__lado_a == self.__lado_b and self.__lado_b == self.__lado_c):
                print("Triangulo equilátero\n") 

class Losango():
    def __init__(self, diagonal_maior, diagonal_menor):
         self.__diagonal_maior = diagonal_maior
         self.__diagonal_menor = diagonal_menor
    def get_area(self):
         return self.__diagonal_maior * self.__diagonal_menor/2.0
    def get_altura(self):
         pass

class Circulo():
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
         return self.__raio

    def get_area(self):
         return pi * self.__raio**2
    def get_circunferencia(self):
        return 2 * pi * self.__raio
    

def main():
     circ1 = Circulo(15)
     print(f'Area do circulo de raio {circ1.get_raio()} = {circ1.get_area()}')
     
if __name__ == "__main__":
    main()