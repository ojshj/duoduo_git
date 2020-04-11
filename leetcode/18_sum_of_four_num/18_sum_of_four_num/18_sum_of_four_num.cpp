// 18_sum_of_four_num.cpp : 定义控制台应用程序的入口点。

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#define target 0  //目标值
using namespace std;
vector<int> nums = { 1,0,-1,0,-2,2 };

//打印函数
void Display(vector<int> vtr)
{
	for (int i = 0; i != vtr.size(); ++i)
	{
		cout << vtr[i] << " ";
	}
	cout << endl;
}

int main()
{
	int max_len = nums.size();
	vector<int> tmp;         //记录符合条件的四个数
	vector<vector<int>> vtr; //无重复数组，所有符合条件的数组

	//从数组中拉取四个值
	for (int a = 0; a < max_len - 3; a++)
	{
		for (int b = a + 1; b < max_len - 2; b++)
		{
			for (int c = b + 1; c < max_len - 1; c++)
			{
				for (int d = c + 1; d < max_len; d++)
				{
					//查看这4个数的和是否和target相等
					if (nums[a] + nums[b] + nums[c] + nums[d] == target)
					{
						//相等，添加进临时数组tmp
						tmp.push_back(nums[a]);
						tmp.push_back(nums[b]);
						tmp.push_back(nums[c]);
						tmp.push_back(nums[d]);

						//tmp添加进vtr中
						vtr.push_back(tmp);
						//清空
						tmp.swap(vector<int>());
					}
					else
					{
						continue;
					}
				}
			}
		}
	}
	//对vtr排序
	sort(vtr.begin(), vtr.end());

	//去除相同项
	vtr.erase(unique(vtr.begin(), vtr.end()), vtr.end());

	for (int i = 0; i < vtr.size(); i++)
	{
		Display(vtr[i]);
	}

	int k;
	cin >> k;
	return 0;
}

