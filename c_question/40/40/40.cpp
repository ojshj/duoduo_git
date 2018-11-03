// 40.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <math.h>
#define PI 3.14159
int main()
{
	float r;
	double s,v;
	printf("input r:\n");
	scanf_s("r=%f",&r);
	s=4*PI*pow(r,2);
	v=4.0/3*PI*pow(r,3);
	printf("r=%f,s=%f,v=%f",r,s,v);

	return 0;
}

