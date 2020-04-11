// prime_factor.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#define MAXNUM 100
using namespace std;

int main()
{
	//将所有质数放入prime
	vector<int> prime;
	int flag = 0;
	for (int num = 2; num <= MAXNUM; num++)
	{
		flag = 0;
		for (int i = 2; i <= sqrt(num); i++)
		{
			if (num%i == 0)
			{
				flag = 1;
				break;
			}
		}
		if (flag == 0)
		{
			prime.push_back(num);
		}
	}

	int tmp;
	vector<int> result;
	//将每三个质数相乘，结果放入result中
	for (int i = 0; i < prime.size()-2; i++)
	{
		for (int j = i+1; j <prime.size() - 1; j++)
		{
			for (int k = j + 1; k < prime.size(); k++)
			{
				tmp = prime[i] * prime[j] * prime[k];
				result.push_back(tmp);
			}
		}
	}

	//排序，打印前5个
	sort(result.begin(), result.end());
	for (int i = 0; i < 5; i++)
	{
		cout << result[i] << endl;
	}

	int z;
	cin >> z;
    return 0;
}

