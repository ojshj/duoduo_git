// 18_sum_of_four_num.cpp : �������̨Ӧ�ó������ڵ㡣

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#define target 0  //Ŀ��ֵ
using namespace std;
vector<int> nums = { 1,0,-1,0,-2,2 };

//��ӡ����
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
	vector<int> tmp;         //��¼�����������ĸ���
	vector<vector<int>> vtr; //���ظ����飬���з�������������

	//����������ȡ�ĸ�ֵ
	for (int a = 0; a < max_len - 3; a++)
	{
		for (int b = a + 1; b < max_len - 2; b++)
		{
			for (int c = b + 1; c < max_len - 1; c++)
			{
				for (int d = c + 1; d < max_len; d++)
				{
					//�鿴��4�����ĺ��Ƿ��target���
					if (nums[a] + nums[b] + nums[c] + nums[d] == target)
					{
						//��ȣ���ӽ���ʱ����tmp
						tmp.push_back(nums[a]);
						tmp.push_back(nums[b]);
						tmp.push_back(nums[c]);
						tmp.push_back(nums[d]);

						//tmp��ӽ�vtr��
						vtr.push_back(tmp);
						//���
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
	//��vtr����
	sort(vtr.begin(), vtr.end());

	//ȥ����ͬ��
	vtr.erase(unique(vtr.begin(), vtr.end()), vtr.end());

	for (int i = 0; i < vtr.size(); i++)
	{
		Display(vtr[i]);
	}

	int k;
	cin >> k;
	return 0;
}

