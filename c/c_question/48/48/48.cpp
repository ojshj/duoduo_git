// 48.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	int n,k,m;
	printf("please input n,k:\n");
	scanf_s("n=%d,k=%d",&n,&k);
	m=n^1<<(k-1);
	printf("\nm=%d",m);
	return 0;
}

