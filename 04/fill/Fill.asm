// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.
//
//PSUDO CODE:
	//IF (Ox6000 != 0)
		//THEN (0x4000 --> Screen Last Address)
			//Screen = 1 (BLACK)
		//ELSE ()
			//Screen = 0 (WHITE)
	//D - DATA 
	//A - ADDRESS OF MEMORY (but could be data)
	//M - IS DATA VALUE AT A
//
@KBD
D=A

@ENDOFSCREEN
M=D-1

@SCREEN
D=A

@SCREENINDEX
M=D

(WHITE)
	@SCREENINDEX	//Load Current screen index into D
	A=M
	M=0		//Set the color of the screen

	@SCREENINDEX	
	D=M

	@ENDOFSCREEN	//Math to check if current index is end of screen
	D=D-M

	@SCREENINDEX	//Incriment the screen index by 1
	M=M+1

	@READ		//Statement to check if screen index is out of bounds 
	D;JEQ

	@WHITE
	0;JMP

(READ)
	@SCREEN		//Load the address of the start of the screen into D
	D=A

	@SCREENINDEX	//Reset the counter that we use to index through the screen
	M=D		//Resets to the first index of the screen

	@KBD	//Store (@) KBD in address A
	D=M	//Load the value of M @ A into D
	//CHECK IF BUTTON HAS BEEN PRESSED
	@BLACK	//Store (@) BLACK in address A
	D;JNE	//if D != 0, Jump to black label
	//IF BUTTON HAS NOT BEEN PRESSED
	@WHITE
	D;JEQ	//if D == 0, 

(BLACK)
	@SCREENINDEX	//Load Current screen index into D
	A=M
	M=-1		//Set the color of the screen

	@SCREENINDEX	
	D=M

	@ENDOFSCREEN	//Math to check if current index is end of screen
	D=D-M

	@SCREENINDEX	//Incriment the screen index by 1
	M=M+1

	@READ		//Statement to check if screen index is out of bounds 
	D;JEQ

	@BLACK
	0;JMP

