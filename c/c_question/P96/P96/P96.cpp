// P96.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

int main()
{
	int value, ok, number, cs, cnt;
	clrscr();
	ok = 0;
	cnt = 0;
	randomize();
	value = rand();
	printf("please enter the maximum allowed number of guesses: ",value);
	scanf_s("%d", &number);
	do 
	{
		printf("please input the guess number(%d): ", cnt + 1);
		scanf_s("%d", &number);
		if (number == value)
			ok = 1;
		else if (number > value)
			printf("Result:%d Too big!!!\n", number);
		else
			printf("Result:%d Too small!!!\n", number);
		cnt++;
	}
	while (cnt<cs&&ok!=1);
	if (ok == 1)
		printf("Congradulation,you win!!\n");
	else
		printf("sorry,you have exceeded the maximum number of allowed\n the answer is :%d", value);
	int i;
	cin >> i;
    return 0;
}

