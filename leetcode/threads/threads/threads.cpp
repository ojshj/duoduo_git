// threads.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <numeric>
#include <mutex>
#include <thread>
using namespace std;

mutex mtx;

//��׼�̺߳���ֻ�ܷ���void�������Ҫ���߳��з���ֵ�������ô������õķ���
void GetSumT(vector<int>::iterator first, vector<int>::iterator last, int &result)
{
	mtx.lock();
	result = accumulate(first, last, 0); //�ۼ���ͺ���
	// ǰ����������쳣��unlock �͵������ˡ�
	mtx.unlock();
}

int main() //���߳�
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

	//�ֶ�������
	thread first(GetSumT, largeArrays.begin(), largeArrays.begin() + 20000000, ref(result1)); //���߳�1
	thread second(GetSumT, largeArrays.begin() + 20000000, largeArrays.begin() + 40000000, std::ref(result2)); //���߳�2
	thread third(GetSumT, largeArrays.begin() + 40000000, largeArrays.begin() + 60000000, std::ref(result3)); //���߳�3
	thread fouth(GetSumT, largeArrays.begin() + 60000000, largeArrays.begin() + 80000000, std::ref(result4)); //���߳�4
	thread fifth(GetSumT, largeArrays.begin() + 80000000, largeArrays.end(), std::ref(result5)); //���߳�5

	first.join(); //�������������߳�Ҫ�ȴ����߳�ִ����ϣ�����ִ����һ��
	second.join();
	third.join();
	fouth.join();
	fifth.join();

	int resultSum = result1 + result2 + result3 + result4 + result5; //���ܸ������̵߳Ľ��
	cout << resultSum;

	int k;
	cin >> k;
	return 0;
}
