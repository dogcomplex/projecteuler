#include <stdio.h>

int bitcount_naive(int n)
{
   int count = 0;
   while(n != 0){
      if (n&1){ count++; }
      n >>= 1;
   }
   return count;
}

int bitcount_hacky(int n)
{
   // fastest I could think of. Adds every 2 bits, then every 4, every 8, etc
   n = (n & 0x55555555)+((n & 0xAAAAAAAA)>>1); //_1_1 + 1_1_>>1
   n = (n & 0x33333333)+((n & 0xCCCCCCCC)>>2); //__11 + 11__>>2
   n = (n & 0x0F0F0F0F)+((n & 0xF0F0F0F0)>>4); //etc
   n = (n & 0x00FF00FF)+((n & 0xFF00FF00)>>8);
   return (n & 0x0000FFFF)+((n & 0xFFFF0000)>>16); 

   // still uses 20 bitwise operations.
}


 
int main()
{
   int n = 6;
   printf("Enter an integer\n");
   scanf("%d",&n);
   printf("Bitcount:\n");
   printf("%d\n", bitcount_naive(n));
   printf("%d\n", bitcount_hacky(n));
   return 0;
}


