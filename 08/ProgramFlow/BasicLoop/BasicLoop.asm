@256
D=A
@SP
M=D
// 	push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// 	pop local 0         
@SP
M=M-1
A=M
D=M
@R13
M=D
@1
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
// 	label LOOP
(LOOP)
// 	push argument 0
@2
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push local 0
@1
D=M
@0
A=D+A
D=M
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
// 	pop local 0	        
@SP
M=M-1
A=M
D=M
@R13
M=D
@1
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
// 	push argument 0
@2
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	push constant 1
@1
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
// 	pop argument 0      
@SP
M=M-1
A=M
D=M
@R13
M=D
@2
D=M
@0
D=D+A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
// 	push argument 0
@2
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// 	if-goto LOOP        
@SP
M=M-1
A=M
D=M
@R13
M=D
@R13
D=M
@LOOP
D;JNE
// 	push local 0        
@1
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
