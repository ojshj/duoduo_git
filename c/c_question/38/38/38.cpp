// 38.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <math.h>


int main()
{
	float a,b,c,p,s;
	printf("\nplease3 input 3 numbers:\n");
	scanf_s("%f,%f,%f",&a,&b,&c);
	p=(a+b+c)/2;
	s=sqrt(p*(p-a)*(p-b)*(p-c));
	printf("\ns=%.2f",s);

	return 0;
}

