// P93.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	int day, x;
	day = 9;
	x = 1;
	while (day > 0)
	{
		x = (x + 1) * 2;
		day--;
	}
	printf("\n %d the total is %d", day + 1, x);
	int i;
	cin >> i;
	return 0;
}

