// 58.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <math.h>

int main()
{
	int a,b,c;
	float p,area;
	clrscr();
	printf("\n please input the 3 side of the triangle: ");
	scanf_s("%d,%d,%d",&a,&b,&c);
	area=0;
	if(a+b>c&&a+c>b&&b+c>a)
	{
		p=(a+b+c)/2;
		area=sqrt(p*(p-a)*(p-b)*(p-c));
	}
	printf("\n the area of triangle is:%5.2f\n",area);
	return 0;
}

