// c 1.1.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include <stdio.h>
#include "stdafx.h"
#include<iostream>
using namespace std;

int main()
{
	int x, y;
	for(x=1;x<=9;x++)
	{
		for (y = 1; y <= x; y++)
			printf("%d*%d=%d", x, y, x*y);
		printf("\n");
	}
	int i;
	cin >> i;

	return 0;
}

