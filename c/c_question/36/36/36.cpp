// 36.cpp : 定义控制台应用程序的入口点。
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

