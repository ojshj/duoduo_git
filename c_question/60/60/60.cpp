// 60.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int year;
	printf("lplease input year:");
	scanf_s("%d",&year);
	if (year%4==0&&year%100==0||year%400==0)
		printf("yea\n");
	else
		printf("no\n");

	return 0;
}

