#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double x_1,x_2,y_1,y_2;
double square(double x)
{
	return x*x;
}

double distance(void)
{
	return square(x_2 - x_1) + square(y_2 - y_1);
}

int main(void)
{
	double steps = 1000000000;
	double inside_circle = 0;

	for (int i = 0 ; i < steps ; i++)
	{
		x_1 = (double)rand() / RAND_MAX;
		y_1 = (double)rand() / RAND_MAX;
		x_2 = 0;
		y_2 = 0;
		double d = distance();
		if (d <= 1)
		{
			inside_circle +=1;
		}
	}
	double pi = 4*(inside_circle/steps);
	printf("Value for pi for %f steps: %f\n", steps,pi);
}

/* to run it
gcc pi.c -o pi
./pi
*/
