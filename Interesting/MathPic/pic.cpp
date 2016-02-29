// NOTE: compile with g++ filename.cpp -std=c++11

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define DIM 1024
#define DM1 (DIM-1)
#define _sq(x) ((x)*(x)) // square
#define _cb(x) abs((x)*(x)*(x)) // absolute value of cube
#define _cr(x) (unsigned char)(pow((x),1.0/3.0)) // cube root

unsigned char GR(int,int);
unsigned char BL(int,int);

unsigned char RD(int i,int j){
	if(17*_sq(j) -16*abs(j)*i + 17*_sq(i) < 2550) return 0;
	return 255;
}

unsigned char GR(int i,int j){
	int x = i,y = j; 
	i = (512-i)/20;
	j = (512-j)/20;
	if(17*_sq(j) -16*abs(j)*i + 17*_sq(i) < 2550) return x/10 + y/10;
	return 255;
}

unsigned char BL(int i,int j){
	if(17*_sq(j) -16*abs(j)*i + 17*_sq(i) < 2550) return 0;
	return 255;
}

void pixel_write(int,int);
FILE *fp;

int main(){
	srand(time(0));
	fp = fopen("MathPic.ppm","wb");
	fprintf(fp, "P6\n%d %d\n255\n", DIM, DIM);
	for(int j=0;j<DIM;j++)
		for(int i=0;i<DIM;i++)
			pixel_write(i,j);
	fclose(fp);
	return 0;
}

void pixel_write(int i, int j){
	static unsigned char color[3];
	color[0] = RD(i,j)&255;
	color[1] = GR(i,j)&255;
	color[2] = BL(i,j)&255;
	fwrite(color, 1, 3, fp);
}
