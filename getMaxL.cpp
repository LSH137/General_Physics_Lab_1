#include<stdio.h>
#include<math.h>

#define h 0.939 //m
#define v0 3.55 // m/s
#define g 9.798 //m/s^2

#define epsilon 0.001
#define step 0.0001
#define PI 3.141592

double getL(double theta)
{
    double result;
    result = v0*cos(theta)*((v0*sin(theta)/g)*(v0*sin(theta)/g) + 2*h/g);
    return result;
}


double dLdTheta(double theta)
{
    double result;
    double temp1;
    double temp2;

    temp1 = 1/g + v0*sin(theta) / (2 * sqrt( (v0*sin(theta))*(v0*sin(theta)) + 2*g*h));
    temp2 = v0*sin(theta)/g + sqrt((v0*sin(theta)/g)*(v0*sin(theta)/g)+2*h/g);
    
    result = v0*v0*cos(theta)*cos(theta)*temp1 - v0*sin(theta)*temp2;
    return result;
}

int main(void)
{
    double rad = 0.0;
    double result;
    int findroot = 0;

    while(rad < PI/2.0)
    {
        result = dLdTheta(rad); 
        if(abs(result) < epsilon)
        {
            findroot = 1;
            break;
        }
        
        rad = rad + step;
        printf("angle: %lf(rad)\t dL/dtheta: %lf\n", rad, result);
    }
    if(findroot == 0)
        printf("no answer was founded\n");
    else
    {
        printf("\n=======================================\n");
        printf("answer: %lf(rad)\t result: %lf\t L: %lf\n", rad, result, getL(rad));
    }

    return 0;   
}