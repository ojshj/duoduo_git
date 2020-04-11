// c++ 1.4.2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	int sum = 0;
	for (int val = 0; val <= 10; ++val)
		sum += val;
	std::cout << "sum of 1 to 10 is " << sum << std::endl;
	
	int i;
	cin >> i;
	return 0;
}

