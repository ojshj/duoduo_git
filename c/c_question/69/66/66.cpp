// 66.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	int x,fx;
	printf("please input x:");
	scanf_s("%d",&x);
	if(x>=0)
		if(x<=5)
			fx=5;
		else
			fx=10;
	else if (x>=-5)
		fx=-5;
	else
		fx=-10;
	printf("f(x)=%d\n",fx);
	return 0;
}

