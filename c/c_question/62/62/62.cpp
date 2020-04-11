// 62.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	char ch;
	printf("\nplease input character:");
	scanf_s("%c",&ch);
	if (ch>='a'&&ch<='z')
		ch=ch-32;
	else
		ch=ch;
	printf("%c\n",ch);
	return 0;
}

