@count
M=0

@R2
M=0;

(MULT)
	@count
	D=M	//Move count into data

	@R0
	D=D-M	//Take input 0 and subtract it from the count

	@END
	D;JEQ

	@count	
	M=M+1	//Index the count by 1 saying we have added the number once

	@R1	//Load the value of number 2 into D
	D=M

	@R2	//Adds the current output with R1
	M=M+D

	@MULT
	0;JMP


(END)
	@END
	0;JMP	//Infiinite Loop


// 3 X 4 = 12
// R0 X R1 = R2

