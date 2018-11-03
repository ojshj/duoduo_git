// 41.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	float height,weight1,weight2;
	printf("please input you height:\n");
	scanf_s("%f",&height);
	weight1=18*height*height;
	weight2=25*height*height;
	printf("you should control your weight between %.lf and %.lf",weight1,weight2);
	return 0;
}

