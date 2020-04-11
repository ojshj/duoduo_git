// 34.cpp : 定义控制台应用程序的入口点。
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

