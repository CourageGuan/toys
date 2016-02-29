#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>

const int sz = 15;
const int maxn = sz*sz + 2;

class Chess
{
public:
	int r,c;
	int id,color; //Black 1  White 2
	Chess() {}
	Chess(int id,int color,int r,int c):id(id),color(color),r(r),c(c) {}
};


class Board
{
public:
	int board[sz][sz];
	Chess chess[maxn];
	int tot;
	Board()
	{
		memset(board,0,sizeof board);
		tot = 0;
	}

	bool inside(int r,int c)
	{
		return r>=0 && c>=0 && r<sz && c<sz;
	}

	bool put(int col,int r,int c)
	{
		--r,--c;
		if(!inside(r,c) || board[r][c]) return false;
		board[r][c] = col;
		chess[tot] = Chess(tot++,col,r,c);
		return true;
	}

	bool check(int r,int c)
	{
		--r,--c;
		int col = board[r][c];
		int x = r,y = c;
		int cnt = -1;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			++y;
		}
		x = r,y = c;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			--y;
		}
		if(cnt >= 5) return true;

		x = r,y = c;
		cnt = -1;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			++x;
		}
		x = r,y = c;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			--x;
		}
		if(cnt >= 5) return true;

		x = r,y = c;
		cnt = -1;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			++x,++y;
		}
		x = r,y = c;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			--x,--y;
		}
		if(cnt >= 5) return true;

		x = r,y = c;
		cnt = -1;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			++x,--y;
		}
		x = r,y = c;
		while(inside(x,y) && board[x][y] == col)
		{
			++cnt;
			--x,++y;
		}
		if(cnt >= 5) return true;

		return false;
	}

	void show()
	{
		for(int i=0;i<sz;++i)
		{
			for(int j=0;j<sz;++j)
				putchar(board[i][j]?(board[i][j]==1?'B':'W'):'.');
			puts("");
		}
		puts("");
	}

};

class Player
{
public:
	char name[22];
	int color;
	int type;
	Player() {}
	Player(char *name,int color,int type):color(color),type(type)
	{
        memcpy(this -> name,name,sizeof(this -> name));
	}

	bool put(Board& board,int r,int c)
	{
		return board.put(color,r,c);
	}

	bool win(Board& board,int r,int c)
	{
		return board.check(r,c);
	}

	bool take(Board& board)
	{
		int r,c;
		if(type == 0)
		{
			do
			{
				printf("Input Pos(r,c):"); scanf("%d %d",&r,&c);
				if(put(board,r,c)) break;
				else puts("Please Input A Correct Pos!");
			}while(1);
		}
		else
		{
			do
			{
				r = rand()%sz + 1;
				c = rand()%sz + 1;
			}while(!put(board,r,c));
		}
		printf("%d %d\n",r,c);
		return win(board,r,c);
	}
};

int main()
{
	//freopen("test.txt","r",stdin);
	srand(time(0));
	Board game;
	Player p[2];
	for(int i=0;i<2;++i)
	{
		char name[22],type[22];
		printf("Player %d (%s):\n",i+1,i&1?"White":"Black");
		printf("Name: "); scanf("%s",name);
		printf("Type(Peo or PC): "); scanf("%s",type);
		p[i] = Player(name,i+1,type[1] == 'C'?1:0);
	//	printf("name:%s\ncolor:%d\ntype:%d\n",p[i].name,p[i].color,p[i].type);
	}
	game.show();
	while(1)
	{
		if(game.tot > sz*sz)
		{
			puts("Tie");
			break;
		}
		if(p[0].take(game))
		{
			game.show();
			printf("%s Win!",p[0].name);
			break;
		}
		puts("ok");
		game.show();
		if(game.tot > sz*sz)
		{
			puts("Tie");
			break;
		}
		if(p[1].take(game))
		{
			game.show();
			printf("%s Win!",p[1].name);
			break;
		}
		game.show();
	}
	return 0;
}
