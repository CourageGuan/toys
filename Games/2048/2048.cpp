//2048@GYH
#include<iostream>
#include<ctime>
#include<cstdlib>
#include<iomanip>
//#include<cconio>
using namespace std;
const int n = 4, N = 6;

int back[7][7];

void print(void);
void randoms(void);
int judgemove(char);
int judgelife(char);
int judgewin();
void move(char);

int main()
{
	cout << "Welcome to 2048 @GYH" << endl;
	for (int i = 0; i <= N; i++)
		for (int j = 0; j <= N; j++)
		{
			back[i][j] = 0;
			if (i == 0 || i == N || j == 0 || j == N)
				back[i][j] = -1;
		}
	randoms();
	print();
	while (1)
	{
		char ch;
		cout << "Please input a char(W/S/A/D):";
		cin >> ch;
		while (ch != 'W' && ch != 'S' && ch != 'A' && ch != 'D'
			   && judgemove(ch) == 0)
		{
			cout << "ERROR!!!Wrong char OR Can't move...\nPlease input again:";
			cin >> ch;
		}
		if (judgelife(ch))
		{
			move(ch);
			//clrscr();
			system("cls");
			print();
			randoms();
			//clrscr();
			system("cls");
			print();
			// system("cls");
	    }
		else
			break;
		if (judgewin())
		{
			cout << "You Win!" << endl;
			return 0;
		}
	}
	cout << "You lose!" << endl;
	return 0;
}

void print(void)
{
	cout << "2048@GYH" << endl;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			if (back[i][j] == 0)
				cout << setw(4) << "[ ]";
			else
				cout << setw(4) << back[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

void randoms(void)
{
	int i = 1, j = 0;
	while (back[i][j] != 0)
	{
		srand(time(0));
		i = rand() % (n - 1) + 1;
		j = rand() % (n - 1) + 1;
	}
	int t = rand() % 9;
	if (t > 7)
		back[i][j] = 4;
	else
		back[i][j] = 2;
}

int judgemove(char ch)
{
	switch (ch)
	{
	case 'W':
		{
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (back[i - 1][j] == 0 || back[i - 1][j] == back[i][j])
						return 1;
			break;
		}
	case 'S':
		{
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (back[i + 1][j] == 0 || back[i + 1][j] == back[i][j])
						return 1;
			break;
		}
	case 'A':
		{
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (back[i][j - 1] == 0 || back[i][j - 1] == back[i][j])
						return 1;
			break;
		}
	case 'D':
		{
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (back[i][j + 1] == 0 || back[i][j + 1] == back[i][j])
						return 1;
			break;
		}
	}
	return 0;
}

int judgelife(char ch)
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (!back[i][j])
				return 1;
	return judgemove(ch);
}

int judgewin()
{
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (back[i][j] == 2048)
				return 1;
	return 0;
}

void move(char ch)				// PROBLEM!
{
	switch (ch)
	{
	case 'W':
		{
			for (int j = 1; j <= n; j++)
				for (int k = 1; k <= n; k++)
					for (int i = 1; i <= n; i++)
					{
						if (back[i][j] == 0 && back[i + 1][j] != -1)
						{
							swap(back[i][j], back[i + 1][j]);
							// break;
						}
						if (back[i][j] == back[i + 1][j]
							&& back[i + 1][j] != -1)
						{
							back[i][j] += back[i + 1][j];
							back[i + 1][j] = 0;
						}
					}
			break;
		}
	case 'S':
		{
			for (int j = 1; j <= n; j++)
				for (int k = 1; k <= n; k++)
					for (int i = n; i >= 1; i--)
					{
						if (back[i][j] == 0 && back[i - 1][j] != -1)
						{
							swap(back[i][j], back[i - 1][j]);
							// break;
						}
						if (back[i][j] == back[i - 1][j]
							&& back[i - 1][j] != -1)
						{
							back[i][j] += back[i - 1][j];
							back[i - 1][j] = 0;
						}
					}
			break;
		}
	case 'A':
		{
			for (int i = 1; i <= n; i++)
				for (int k = 1; k <= n; k++)
					for (int j = 1; i <= n; j++)
					{
						if (back[i][j] == 0 && back[i][j + 1] != -1)
						{
							swap(back[i][j], back[i][j + 1]);
							// break;
						}
						if (back[i][j] == back[i][j + 1]
							&& back[i][j + 1] != -1)
						{
							back[i][j] += back[i][j + 1];
							back[i][j + 1] = 0;
						}
					}
			break;
		}
	case 'D':
		{
			for (int i = 1; i <= n; i++)
				for (int k = 1; k <= n; k++)
					for (int j = n; j >= 1; j--)
					{
						if (back[i][j] == 0 && back[i][j - 1] != -1)
						{
							swap(back[i][j], back[i][j - 1]);
							// break;
						}
						if (back[i][j] == back[i][j - 1]
							&& back[i][j - 1] != -1)
						{
							back[i][j] += back[i][j - 1];
							back[i][j - 1] = 0;
						}
					}
			break;
		}
	}
}

