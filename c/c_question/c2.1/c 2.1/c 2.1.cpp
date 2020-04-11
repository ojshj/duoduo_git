// c 2.1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<stdio.h>
#include<iostream>
using namespace std;


int main()
{
	char c;
	scanf("%c", &c);
	c += 32;
	putchar(c);
    
	int i;
	cin >> i;

	return 0;
}

