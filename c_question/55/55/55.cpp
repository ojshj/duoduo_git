// 55.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int a,b,max;
	printf("please input 2 integer data:\n");
	scanf_s("%d,%d",&a,&b);
	max=a;
	if (max<b)
		max=b;
	printf("the max is:%d\n",max);
	return 0;
}

