// test1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

int main()
{
    int num1,bai,shi,ge,num2;
	printf("please input num1:");
	scanf_s("%d",&num1);
	bai=num1/100;
	shi=num1%100/10;
	ge=num1/10;
	num2=ge*100+shi*10+bai;
	printf("\n%d inverse number is %d\n",num1,num2);
	 
	return 0;
}
