// 1.4.3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	std::cout << "enter 2 numbers: " << std::endl;
	int v1, v2;
	std::cin >> v1 >> v2;
	int lower, upper;
	if (v1 <= v2)
	{
		lower = v1;
		upper = v2;
	}
	else {
		lower = v2;
		upper = v1;
	}
	int sum = 0;
	for (int val = lower; val = upper; ++val)
	{
		sum += val;
	}
	std::cout<< "sum of" << lower << "to" << upper << "is" << sum << std::endl;
	int i;
	cin >> i;
	return 0;
}

