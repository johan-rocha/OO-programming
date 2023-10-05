// https://pt.stackoverflow.com/questions/240500/heran%C3%A7a-com-construtores

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
using namespace std;

class Ponto
{
    private:
        int x, y;
    public:
        Ponto(int x_point, int y_point)
        {
            x = x_point;
            y = y_point;
        }

        void showCoordinates();
        float distanciaDestePonto(int other_x, int other_y);
        int getX()
        {
            return x;
        }
        int getY()
        {
            return y;
        }

        ~Ponto(){}
};

void Ponto::showCoordinates()
{
    cout << "coordinates: " << "(" << x << "," << y << ")" << endl;
}

float Ponto::distanciaDestePonto(int other_x, int other_y)
{
    return abs(sqrt(pow(other_x - x, 2) + pow(other_y - y, 2)));
}

class Reta : private Ponto
{
    private:

        Ponto ponto_1, ponto_2;
        
    public:


        Reta(int x_1, int y_1, int x_2, int y_2) : Ponto(x_1, y_1), ponto_1(x_1, y_1), ponto_2(x_2, y_2){} //rever como funciona esse contrutor

        float comprimentoReta();

        ~Reta(){}
};

float Reta::comprimentoReta()
{
    return ponto_1.distanciaDestePonto(ponto_2.getX(), ponto_2.getY());
}

class Retangulo
{
    protected:
        int base, altura;
    public:

        Retangulo(int base_init, int altura_init)
        {
            base = base_init;
            altura = altura_init;
        }
        int get_base();
        int get_altura();
        int get_area();
        int get_perimetro();
        bool eh_quadrado();

        ~Retangulo(){}
};

int Retangulo::get_base()
{
    return base;
}

int Retangulo::get_altura()
{
    return altura;
}

int Retangulo::get_area()
{
    return base * altura;
}

int Retangulo::get_perimetro()
{
    return 2 * base + 2 * altura;
}

bool Retangulo::eh_quadrado()
{
    if(base == altura)
        return true;
    else
        return false;
}

class Triangulo
{
    protected:
        int lado_a, lado_b, lado_c;

    public:
        Triangulo(int lado_a_input, int lado_b_input, int lado_c_input)
        {
            lado_a = lado_a_input;
            lado_b = lado_b_input;
            lado_c= lado_c_input;
        }
        float get_area();
        float get_altura_relativa(int lado_base);
        int get_perimetro();
        void show_tipo();
        
        ~Triangulo(){}
};

float Triangulo::get_area() //formula de Heron
{
    float semiperimetro = (lado_a + lado_b + lado_c)/2.0;

    return sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c));
}

float Triangulo::get_altura_relativa(int lado_base)
{
    return (get_area()/lado_base);
}

int Triangulo::get_perimetro()
{
    return (lado_a + lado_b + lado_c);
}

void Triangulo::show_tipo()
{   
    if(lado_a == lado_b && lado_b == lado_c)
        cout << "Triângulo equilátero" << endl;
    else if(lado_a == lado_b || lado_a == lado_c || lado_b == lado_c)
        cout << "Triangulo isósceles" << endl;
    else
        cout << "Triângulo escaleno" << endl;
}

class Losango
{
    protected:
        int diagonal_maior, diagonal_menor;
    public:
        Losango(int diagonal_maior_input, int diagonal_menor_input)
        {
            diagonal_maior = diagonal_maior_input;
            diagonal_menor = diagonal_menor_input;
        }

        int get_area();
        float get_lado();
        int get_altura();
        int get_perimetro();

        ~Losango(){}
};

int Losango:: get_area()
{
    return (diagonal_maior * diagonal_menor)/2.0;
}

float Losango::get_lado()
{
    return sqrt(pow(diagonal_maior/2.0, 2) + pow(diagonal_menor/2.0, 2));
}

int Losango::get_altura()
{
    return get_area()/get_lado();
}

int Losango::get_perimetro()
{
    return 4 * get_lado();
}

class Circulo
{
    protected:
        int raio;
    public:
        Circulo(int raio_input)
        {
            raio = raio_input;
        }

        int get_raio();
        float get_area();
        float get_circunferencia();

        ~Circulo(){}
};

int Circulo::get_raio()
{
    return raio;
}

float Circulo::get_area()
{
    return M_PI * pow(raio, 2);
}

float Circulo::get_circunferencia()
{
    return 2 * M_PI * raio;
}


int main()
{
    Reta reta_teste(10, 10, 20, 20);
    cout << "O comprimento da reta AB = "<< fixed << setprecision(6) << reta_teste.comprimentoReta() << endl;

    Retangulo retangulo_teste(10, 20);
    cout << "\neh quadrado? : " << (retangulo_teste.eh_quadrado() ? "Sim" : "Não") << endl;
    cout << "area do retangulo = " << retangulo_teste.get_area() << endl;

    Triangulo equilatero(5, 5 ,5);
    equilatero.show_tipo();

    Triangulo isosceles(3, 5, 5);
    isosceles.show_tipo();

    Triangulo escaleno(7, 8, 9);
    escaleno.show_tipo();
    cout << "Area do escaleno = " << escaleno.get_area() << endl;
    cout << "Perimetro do escaleno = " << escaleno.get_perimetro() << endl;
}