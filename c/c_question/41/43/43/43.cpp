// 43.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"


int main()
{
	int a,k,n;
	printf("input a:");
    scanf_s("%d",&a);
	printf("\ninput k:");
	scanf_s("%d",&k);
	a>>=k-1;
	n=a&1;
	printf("\nn=%d",n);
	return 0;
}

