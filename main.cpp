#include "my.h"
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int start,length;
bool win;
short x[102];
short* p, * l;
string st;
void AnswerPrint()
{
	for (int i = 0; i <= length - 1; i++)
	{
		cout << *(p + i) << endl;
	}
	return;
}
int GameMode1()
{
	cout << "Start Number:";
	cin >> start;
	cout << "Length(<=99):";
	cin >> length;
	if (length > 99)
	{
		cout << "Length Too Long!" << endl;
		system("pause");
		return 0;
	}
	p = RandomNumber(start, length);
	cout << "Game Ready!" << endl;
	cout << "Start!" << endl;
	int k = 1;
	while (win == false)
	{
		cout << ">Turn" << k << ":";
		memset(x, 0, sizeof(x));
		bool f = false;
		for (int i = 0; i <= length - 1; i++)
		{
			cin >> x[i];
			if (x[i] == -1)
			{
				AnswerPrint();
				f = true;
				break;
			}
		}
		if (f == true)
			continue;
		l = CompareNumber(x, p, length);
		if (*(l + 0) == length)
		{
			cout << "You Win!" << endl;
			win = true;
		}
		else {
			cout << *(l + 0) << " " << *(l + 1) << endl;
		}
		k++;
	}
	return 0;
}
int main()
{
	int error;
	printf("            Welcome To NumberGame      By wzcwzc0  \n");
	printf("******************************************************\n");
	printf("1.游戏模式1:(输入GameMode1运行)                     \n");
	printf("计算机随机生成一组数据，每一回合你输入等长的数据，计算\n");
	printf("机将返回两个数，第一个数为位置正确的数的个数，第二个数\n");
	printf("为数正确但位置错误的数的个数，最终直到你猜中这组数据为止\n");
	printf("******************************************************\n");
	while (st != "exit")
	{
		cout << ">>";
		cin >> st;
		if (st == "GameMode1")
		{
			error=GameMode1();
			printf("\n\n");
			continue;
		}
		cout << "Error Input" << endl;
	}
	system("pause");
	return 0;
}
