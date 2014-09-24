#include <stdio.h>

struct Rect
{
int left;
int top;
int right;
int bottom;
};

typedef struct Rect Rect;

int RIntersect(Rect r1, Rect r2)
{
	if (r1.right <= r1.left || r2.right <= r2.left)
		return 0; // invalid rectangle
	if (r1.right <= r2.left || r2.right <= r1.left)
		return 0; // adjacent in x
	if (r1.top <= r2.bottom || r1.top <= r2.bottom)
		return 0; // adjacent in y
	return 1; 
};

int RIntersectArea(Rect r1, Rect r2)
{
	/*
	This can probably be better. I tried to minimize the number of logic checks,
	but if speed is really the issue there may be better ways to go about it
	(e.g. remove the struct altogether to avoid referencing)
	*/
	int a;
	if (r1.right <= r1.left || r2.right <= r2.left)
		return 0; // invalid rectangle
	if (r1.right <= r2.left || r2.right <= r1.left)
		return 0; // adjacent in x
	if (r1.top <= r2.bottom || r1.top <= r2.bottom)
		return 0; // adjacent in y

	// determine x area
	if (r1.left <= r2.left)
		if (r1.right <= r2.right)
			a = r1.right-r2.left;
		else 
			a = r2.right-r2.left;
	else 
		if (r2.right <= r1.right)
			a = r2.right-r1.left;
		else
			a = r1.right-r1.left;
	// determine y area
	if (r1.bottom <= r2.bottom)
		if (r1.top <= r2.top)
			a *= r1.top-r2.bottom;
		else 
			a *= r2.top-r2.bottom;
	else 
		if (r2.top <= r1.top)
			a *= r2.top-r1.bottom;
		else
			a *= r1.top-r1.bottom;
	
	return a;

};



int main()
{
	Rect test1, test2;
	test1.left = 0;
	test1.right = 10;
	test1.bottom = 0;
	test1.top = 20;
	test2.left = 1;
	test2.right = 5;
	test2.bottom = -1;
	test2.top = 4;

	printf("%d", RIntersectArea(test1,test2));

	return 0;
};