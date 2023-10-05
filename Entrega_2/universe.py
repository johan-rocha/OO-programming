#!/usr/bin/env python3

from math import *
    

class Ponto():
    def __init__(self, x_point, y_point):
        self._x = x_point
        self._y = y_point
    def show_coordinates(self):
        print(f'coordinate point = ({self._x},{self._y})')

    def distancia_deste_ponto(self, other_x, other_y) -> float:
        return abs(sqrt(((other_x - self._x)**2) + ((other_y - self._y)**2)))
    
class Reta(Ponto):
    def __init__(self, x_1, y_1, x_2, y_2):
          self._ponto_1 = Ponto(x_1, y_1)
          self._ponto_2 = Ponto(x_2, y_2)

    def comprimento_reta(self):
        return self._ponto_1.distancia_deste_ponto(self._ponto_2._x, self._ponto_2._y)

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
        return area
    
    def get_altura_relativa(self, lado_base) -> int:
        return self.get_area()/lado_base
    
    def get_perimetro(self) -> int:
        return self.__lado_a + self.__lado_b + self.__lado_c
    
    #pela lei dos cossenos
    def mostrar_tipo(self):

        if(self.__lado_a == self.__lado_b and self.__lado_b == self.__lado_c):
                print("Triangulo equilátero\n")
        elif(self.__lado_a == self.__lado_b or self.__lado_a == self.__lado_c or self.__lado_b == self.__lado_c):
                print("Trigulo isosceles\n")
        else:
                print("Triangulo escaleno\n")

class Losango():
    def __init__(self, diagonal_maior, diagonal_menor):
         self.__diagonal_maior = diagonal_maior
         self.__diagonal_menor = diagonal_menor

    def get_area(self) -> float:
         return self.__diagonal_maior * self.__diagonal_menor/2.0
    
    def get_lado(self) -> float:
         lado = sqrt((self.__diagonal_maior/2.0)**2 + (self.__diagonal_menor/2.0)**2) #teorema de pitagoras
         return lado
    
    def get_altura(self) -> float:
         return self.get_area()/self.get_lado()
    
    def get_perimetro(self) -> float:
         return 4 * self.get_lado()

class Circulo():
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self) -> int:
         return self.__raio

    def get_area(self) -> float:
         return pi * self.__raio**2
    
    def get_circunferencia(self) -> float:
        return 2 * pi * self.__raio
    

def main():
     reta = Reta(10, 10, 20, 20)
     print(f'O comprimento da reta = {reta.comprimento_reta()}')
     
if __name__ == "__main__":
    main()