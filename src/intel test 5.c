#include <stdio.h>

unsigned int CreateSamplerState(
int samplerDisable,
int textureBorderColorMode,
int lodPreClampEnable,
int baseMipLevel,
int mipModeFilter,
int magModeFilter,
int minModeFilter,
float textureLODBias,
int anisotropicAlgorithm)
{
	unsigned int x = 0;

	
	//set sign bit 13
	if (textureLODBias<0){
	  x |= 1 << 13;
	  textureLODBias= -textureLODBias;
	}	
	// set int part (assumes between 0, 16) bits 12:9
	x |= (((int)textureLODBias) & ((1<<5) - 1)) << 9;
	textureLODBias -= (int)textureLODBias;
	//set fraction part, bits 8:1
	float d = 2;
	int i;
	for (i=0; i<8; i++){
		if (textureLODBias >= 1/d){
			x |= 1<< (8 -i);
			textureLODBias -= 1/d;
		}
		d*=2;
	}
	if ((x & (1<<13)) != 0){ // if negative
	  // set to 2s complement
	  x = ((~(x>>1) +1) & ((1<<13) - 1)) << 1;
	  x |= 1<<13;
	}

	x |= anisotropicAlgorithm & 1;  			//bit  0
	x |= (minModeFilter & ((1<<3) - 1)) << 14;  //bits 16:14
	x |= (magModeFilter & ((1<<3) - 1)) << 17;  //bits 19:17
	x |= (mipModeFilter & ((1<<2) - 1)) << 20;  //bits 21:20
	x |= (baseMipLevel & ((1<<5) - 1)) << 22;   //bits 26:22
	// reserve bit 27
	x |= (lodPreClampEnable & 1) << 28; 		//bit  28
	x |= (textureBorderColorMode & 1) << 29; 	//bit  29
	// reserve bit 30
	x |= (samplerDisable & 1) << 31;			//bit  31

	return x;
}

int main(){
	printf("%u",CreateSamplerState(
		1,0,1,(1<<4)+1,0,(1<<2)+1,1,-9.8125,0
		) );
	return 0;
}