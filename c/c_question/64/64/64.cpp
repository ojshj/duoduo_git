// 64.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"


int main()
{
	int score;
	printf("\n please enter an integer score(0-100):");
	scanf_s("%d",&score);
	if (score>100||score<0)
		printf("%d score over range\n",score);
	else if (score>=90)
		printf("A\n");
	else if (score>=80)
		printf("B\n");
    else if (score>=70)
		printf("C\n");
	else if (score>=60)
		printf("D\n");
	else
		printf("E\n");

	return 0;
}

