@256
D=A
@SP
M=D
// 	push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	eq
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@EQUAL2
D;JEQ
@UNEQUAL2
0;JMP
(EQUAL2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_EQ2
0;JMP
(UNEQUAL2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_EQ2)
// 	push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	eq
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@EQUAL3
D;JEQ
@UNEQUAL3
0;JMP
(EQUAL3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_EQ3
0;JMP
(UNEQUAL3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_EQ3)
// 	push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	eq
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@EQUAL4
D;JEQ
@UNEQUAL4
0;JMP
(EQUAL4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_EQ4
0;JMP
(UNEQUAL4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_EQ4)
// 	push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	lt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@LESS2
D;JLT
@NOTLESS2
0;JMP
(LESS2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_LESS2
0;JMP
(NOTLESS2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_LESS2)
// 	push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	lt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@LESS3
D;JLT
@NOTLESS3
0;JMP
(LESS3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_LESS3
0;JMP
(NOTLESS3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_LESS3)
// 	push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	lt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@LESS4
D;JLT
@NOTLESS4
0;JMP
(LESS4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_LESS4
0;JMP
(NOTLESS4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_LESS4)
// 	push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	gt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@GREAT2
D;JGT
@NOTGREAT2
0;JMP
(GREAT2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_GREAT2
0;JMP
(NOTGREAT2)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_GREAT2)
// 	push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	gt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@GREAT3
D;JGT
@NOTGREAT3
0;JMP
(GREAT3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_GREAT3
0;JMP
(NOTGREAT3)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_GREAT3)
// 	push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	gt
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@GREAT4
D;JGT
@NOTGREAT4
0;JMP
(GREAT4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
@END_GREAT4
0;JMP
(NOTGREAT4)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
(END_GREAT4)
// 	push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	add
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D+M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	sub
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	neg
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=0
M=D-M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	and
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D&M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	or
@SP
M=M-1
A=M
D=M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R14
M=D
@R14
D=M
@R13
M=D|M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	not
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
M=!M
@R13
D=M
@SP
A=M
M=D
@SP
M=M+1
