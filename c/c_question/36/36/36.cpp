// 36.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <time.h>
#include <stdib.h>


int main()
{
	srand(time(0));
	printf("%ld",10000+rand()%90000);
	getch();

	return 0;
}

