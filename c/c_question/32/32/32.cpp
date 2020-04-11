// 32.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>


int main()
{
	long original,passward,wan,qian,bai,shi,ge;
	printf("please input original number:");
	scanf_s("%ld",&original);
	ge=original%10;
	shi=original/10%10;
	bai=original/100%10;
	qian=original/1000%10;
	wan=original/10000;
	ge=(ge+8)%10;
	shi=(shi+8)%10;
	bai=(bai+8)%10;
	qian=(qian+8)%10;
	wan=(wan+8)%10;
	passward=ge*10000+qian*1000+bai*100+shi*10+ge;
	printf("\nthe passedward is %d\n",passward);
	return 0;
}

