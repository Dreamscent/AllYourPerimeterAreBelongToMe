#says we gonna use _start as entry point
global _start

#define a memory section
section .text

_start:

 xor    eax,eax
 push   eax
 push   0x22797827
 push   0x70772379
 push   0x73707976
 push   0x70792379
 push   0x73717325
 push   0x72737671
 push   0x20247971
 push   0x24707924
 push   0x71222070
 push   0x77707425
 push   0x79757879
 push   0x75277623
 push   0x27782576
 push   0x73782223
 push   0x22227075
 push   0x73257770
 push   0x70277922
 push   0x75797120
 push   0x77787273
 push   0x70277627
 push   0x71702276
 push   0x77202023
 push   0x23737672
 push   0x25797727
 push   0x71237871
 push   0x22272576
 push   0x75247627
 push   0x72752478
 push   0x25797377
 push   0x24737325
 push   0x75782777
 push   0x25242379
 push   esp
 pop    esi
 mov    edi,esi
 mov    edx,edi
 cld
 mov    ecx,0x80
 mov    ebx,0x41
 xor    eax,eax
 push   eax
 lods   al,BYTE PTR ds:[esi]
 xor    eax,ebx
 stos   BYTE PTR es:[edi],al
 loop   0xb7
 push   esp
 pop    esi
 int3 

section .data

	#defintes a label "message"
	message: db "Hello World!"
	mlen:	equ	$-message #this gets the length of message
	