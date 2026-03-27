#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int steps,trial;
double initial_x,initial_y,r_square;

double square(double x)
{
	return x*x;
}
double average(double y[])
{
	double sum = 0;
	for (int i = 0 ; i < trial ; i++)
	{
		sum += y[i];
	}
	return sum/trial;
}
int main(void)
{
	srand(time(NULL)); /* generates diff seed for each run */
	trial = 1000000;
	steps = 1000;
	double r_square[trial];
	for (int i = 0; i < trial ; i++)
	{
		initial_x = 0;
		initial_y = 0;
		for (int j = 0 ; j < steps ; j++)
		{
			int s_x[] = {-1,1};
			int choice_x = s_x[rand() % 2];  /* rand() generates random number and gives 0 for even 1 for odd so s[0] or s[1] which is -1 and 1 */
			int s_y[] = {-1,1};
			int choice_y = s_y[rand() % 2];
			initial_x += choice_x;
			initial_y += choice_y;
		}
	r_square[i] = square(initial_x) + square(initial_y);
	}
	double avg = average(r_square);
	printf("Average square displacement in 2D: %f\n", avg);
}
