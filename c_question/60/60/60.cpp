// 60.cpp : 定义控制台应用程序的入口点。
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

