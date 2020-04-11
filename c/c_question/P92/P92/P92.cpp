// P92.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<stdio.h>
using namespace std;


int main()
{
	long n;
	printf("\n please input n(>=):");
	scanf_s("%d", &n);
	while (n!=0)
	{
		printf("%d", n % 10);
		n /= 10;
	}
	int i;
	cin >> i;
	return 0;
}

