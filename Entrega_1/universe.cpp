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

class Reta : public Ponto
{
    private:

        Reta(int x_1, int y_1, int x_2, int y_2) : Ponto(x_1, y_1) //revisar
        {
            Ponto ponto_1(x_1, y_1);
            Ponto ponto_2(x_2, y_2);
        }

        float comprimentoReta();

        ~Reta(){}
    public:

};

float Reta::comprimentoReta()
{
    return 
}

int main()
{
    Ponto teste(10, 10);
    teste.showCoordinates();

    cout << "A distancia do ponto (10, 10) ao ponto (20, 20) = "<< fixed << setprecision(6) << teste.distanciaDestePonto(20, 20) << endl;
}