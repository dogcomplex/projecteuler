#include <stdio.h>
#include <stdlib.h>

#define INITSIZE 8  // feel free to set a more reasonable initial size if inappropriate for use

// Stack implementation. Error detection just prints without return status
// dynamicly doubles / halves stack size depending on full or 3/4 empty, repectively

typedef struct STACK
{
	int pos;
	int size;
	int *A;

} Stack;

Stack * CreateStack()
{
	Stack *s;
	s = (Stack *) malloc(sizeof(Stack));
	s->A = (int *) malloc(INITSIZE * sizeof(int));
	
	// memory error
	if (s->A==0)
		printf("Error out of memory\n");
	
	s->size = INITSIZE;
	s->pos = 0;
	return s;
}
void DestroyStack(Stack *s)
{
	free(s->A);
	free(s);
}
void Push(Stack *s, int n)
{
	if (s->pos >= s->size){
		// double stack size (figured I'd go with convention of doubling size when full)
		s->size *=2;
		s->A = (int *) realloc(s->A, 2*s->size * sizeof(int));

		// memory error
		if (s->A==0)
			printf("Error out of memory\n");
	}
	s->A[s->pos++] = n; // store at top, increment
}
int Pop(Stack *s)
{
	if (s->pos>0){
		// halve size of stack if < 1/4 full. feel free to remove if time more important than space
		if (s->pos*4 < s->size){
			s->A = (int *) realloc(s->A, s->size/2 * sizeof(int));
			s->size /=2;

			// memory error
			if (s->A==0)
				printf("Error out of memory\n");
		}	
		return s->A[--s->pos];
	}else
		// empty stack error
		return 1;
	
}

int main(){

	//tests
	Stack *s = CreateStack();
	Push(s,7);
	printf("pos %d\n",s->pos);
	printf("size %d\n",s->size);
	printf("pop %d\n",Pop(s));
	printf("pos %d\n",s->pos);
	printf("size %d\n",s->size);
	Push(s,8);
	Push(s,9);
	Push(s,10);
	printf("pop after push x3 %d\n",Pop(s));
	printf("pop %d\n",Pop(s));
	printf("pos %d\n",s->pos);
	printf("size %d\n",s->size);
	printf("pop %d\n",Pop(s));
	DestroyStack(s);

	return 0;
}