// threads.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <numeric>
#include <mutex>
#include <thread>
using namespace std;

mutex mtx;

//标准线程函数只能返回void，因此需要从线程中返回值往往采用传递引用的方法
void GetSumT(vector<int>::iterator first, vector<int>::iterator last, int &result)
{
	mtx.lock();
	result = accumulate(first, last, 0); //累加求和函数
	// 前面代码如有异常，unlock 就调不到了。
	mtx.unlock();
}

int main() //主线程
{
	int result1, result2, result3, result4, result5;
	
	vector<int> largeArrays;
	for (int i = 0; i < 100000000; i++)
	{
		if (i % 2 == 0)
		{
			largeArrays.push_back(i);
		}
		else
		{
			largeArrays.push_back(-1 * i);
		}
	}

	//分段求和相加
	thread first(GetSumT, largeArrays.begin(), largeArrays.begin() + 20000000, ref(result1)); //子线程1
	thread second(GetSumT, largeArrays.begin() + 20000000, largeArrays.begin() + 40000000, std::ref(result2)); //子线程2
	thread third(GetSumT, largeArrays.begin() + 40000000, largeArrays.begin() + 60000000, std::ref(result3)); //子线程3
	thread fouth(GetSumT, largeArrays.begin() + 60000000, largeArrays.begin() + 80000000, std::ref(result4)); //子线程4
	thread fifth(GetSumT, largeArrays.begin() + 80000000, largeArrays.end(), std::ref(result5)); //子线程5

	first.join(); //阻塞函数，主线程要等待子线程执行完毕，才能执行下一步
	second.join();
	third.join();
	fouth.join();
	fifth.join();

	int resultSum = result1 + result2 + result3 + result4 + result5; //汇总各个子线程的结果
	cout << resultSum;

	int k;
	cin >> k;
	return 0;
}
