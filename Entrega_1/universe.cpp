// https://pt.stackoverflow.com/questions/240500/heran%C3%A7a-com-construtores

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <iomanip>
using namespace std;

class Ponto
{
    private:
        int x;
        int y;
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

        Ponto ponto_1;
        Ponto ponto_2;
        
    public:


        Reta(int x_1, int y_1, int x_2, int y_2) : Ponto(x_1, y_1), ponto_1(x_1, x_2), ponto_2(x_2, y_2){} //rever como funciona esse contrutor

        float comprimentoReta();

        ~Reta(){}
};

float Reta::comprimentoReta()
{
    return ponto_1.distanciaDestePonto(ponto_2.getX(), ponto_2.getY());
}

int main()
{
    Ponto teste(10, 10);
    teste.showCoordinates();

    cout << "A distancia do ponto (10, 10) ao ponto (20, 20) = "<< fixed << setprecision(6) << teste.distanciaDestePonto(20, 20) << endl;
}