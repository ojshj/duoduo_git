// 34.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"


int main()
{
	int a,b,t;
	printf("input 2 numbers: ");
	scanf_s("a=%D,b=%d",&a,&b);
	t=a;
	a=b;
	b=t;
	printf("\nnow a=%d,b=%d\n",a,b);
	return 0;
}

