// 45.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"


int main()
{
	int a,k,b;
	printf("input a and k:\n");
	scanf_s("%d,%d",&a,&k);
	b=a&~(1<<k-1);
	printf("\na=%o,b=%o",a,b);
	return 0;
}

