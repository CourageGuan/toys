//GREEDY SNAKE @GYH
#include<iostream>
#include<conio.h>
#include<ctime>
#include<cmath>
#include<iomanip>
#include<cstdlib>
#define maxN 102
using namespace std;

struct snake
{
	int len;
	int beginx,endx,beginy,endy;
};

snake s;
int back[maxN][maxN];
int n,N;
char flag[maxN][maxN];

void print(void);
void randoms(void);
int judge(char);
void move(char ch,int &beginx,int &beginy,int &endx,int &endy);

int main()
{
	cout<<"Welcome to game GREEDY SNAKE!"<<endl<<"set N as the size(5..20):";
	cin>>n;
	getchar();
	N=n+2;
	for(int i=0;i<=N;i++)
	  for(int j=0;j<=N;j++)
	  {
		  back[i][j]=0;
		  flag[i][j]='D';
	  }
	for(int i=0;i<=N;i++)
	{
		back[0][i]=-1;
		back[i][0]=-1;
		back[N][i]=-1;
		back[i][N]=-1;
	}
	int m=N/2;
	back[m][m]=1;
	back[m][m+1]=1;
	back[m][m-1]=1;
		int t;
	s.len=3;
	t=4;
	s.beginx=m;
	s.beginy=m+1;
	s.endx=m;
	s.endy=m-1;
	randoms();
	print();
	cout<<"OK!Game begin\n";	    char ch='W';
	while(s.len<n*n)
	{
		/*cout<<"Input a char(W/S/A/D):";
		cin>>ch;
		while(ch!='W' && ch!='S' && ch!='A' && ch!='D')
		{
			cout<<endl<<"Error!!!\nAgain please\n";
			cin>>ch;
		}*/
		while(1) 
		{
		if(s.len-t==0) 
		{
		    randoms();
		    t++;
	    } 
	    //print();
		if(judge(ch)) 
		{
			move(ch,s.beginx,s.beginy,s.endx,s.endy);
			if(s.len-t==0) 
		{
		    randoms();
		    t++;
	    }  
		}
		else
		{
			//print();
			cout<<"Game Over\nYou lost at length "<<s.len;
			cout<<t;
			//system("pause");
			return 0;
		}
		//print(); 
		//system("cls");
		clrscr();
		print(); 
		sleep(1);
		if(kbhit())
		{  
		  int t;
		  t=getch();
		  ch=(char)t;
		  	}
		}
	}
	cout<<"You Win!"<<endl;
	//system("pause");
	return 0;	
}

void print(void)
{
	cout<<"GREEDY SNAKE @GYH\n";
	for(int i=0;i<=N;i++)
	{  
	    for(int j=0;j<=N;j++)
	{    if(i==s.beginx&&j==s.beginy)
	    {
	    	cout<<" &";
	    	back[i][j]=3;
		}
	     switch(back[i][j])
	     {
	     	case -1:cout<<" +";break;
	     	case  0:cout<<"  ";break;
	     	case  1:cout<<" *";break;
	     	case  2:cout<<" @";break;	
	     }
   	}
	   cout<<endl;
	}
	cout<<endl;
	back[s.beginx][s.beginy]=1;
}

void randoms(void)    //product @
{
	int x=0,y=0;
	while(back[x][y]!=0)
	{
		srand(time(0));
		x=rand()%(n-1)+1;
		y=rand()%(n-1)+1;
	}
	back[x][y]=2;
}

int judge(char ch)
{
	int x=s.beginx,y=s.beginy;
	switch(ch)
	{
	  case	'W':x--;break;
	  case	'S':x++;break;
	  case	'A':y--;break;
	  case	'D':y++;break;
	}
	if (abs(back[x][y])==1) return 0;  //better way
	return 1;
}

void move(char ch,int &beginx,int &beginy,int &endx,int &endy)  //the most important
{
	switch(ch)
	{
	  case	'W':flag[beginx--][beginy]='W';break;
	  case	'S':flag[beginx++][beginy]='S';break;
	  case	'A':flag[beginx][beginy--]='A';break;
	  case	'D':flag[beginx][beginy++]='D';break;
    }
	/*switch(ch)
	{
	  case	'W':x--;break;
	  case	'S':x++;break;
	  case	'A':y--;break;
	  case	'D':y++;break;
    }*/
    if(back[beginx][beginy]==0) 
	{
		back[endx][endy]=0;
		back[beginx][beginy]=1;
		switch(flag[endx][endy])
		{
		  case 'W':endx--;break;
		  case  'S':endx++;break;
		  case  'A':endy--;break;
		  case  'D':endy++;break;
		}	
	}
	else
	{
		s.len++;
		//back[endx][endy]=0;
		back[beginx][beginy]=1;
	}
}