#include "my.h"
#include <iostream>
#include <string>
#include <stdio.h>
#include <cstdlib>
#include <ctime>
int add(int a, int b)
{
	return a + b;
}
short* RandomNumber(int start, const unsigned int length)
{
	static short num[102];
	srand((unsigned)time(NULL));
	for (int i = 0; i <= length - 1; i++)
	{
		num[i] = rand() % length + start + 2;
	}
	return num;
}
short* CompareNumber(short x[102], short* p, int length)
{
	static short num[3];
	short d[103];
	memset(num, 0, sizeof(num));
	memset(d, 0, sizeof(d));
	for (int i = 0; i <= length - 1; i++)
	{
		if (x[i] == *(p + i))
		{
			num[0]++;
			d[i] = 1;
		}
	}
	for (int i = 0; i <= length - 1; i++)
	{
		if (d[i] == 0)
		{
			for (int j = 0; j <= length - 1; j++)
			{
				if (d[j] == 0 && *(p + j) == x[i])
				{
					num[1]++;
					break;
				}
			}
		}
	}
	return num;
}
