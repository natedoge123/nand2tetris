// 	function SimpleFunction.test 2
(SimpleFunction.test)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
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
// 	push local 1
@1
D=M
@1
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
// 	push argument 1
@2
D=M
@1
A=D+A
D=M
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
// 	return
@LCL
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
@R15
M=D
@R15
D=M
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@R13
M=D
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
@ARG
D=M
D=D+1
@SP
M=D
@R15
D=M
D=D-1
A=D
D=M
@THAT
M=D
@R15
D=M
D=D-1
D=D-1
A=D
D=M
@THIS
M=D
@R15
D=M
D=D-1
D=D-1
D=D-1
A=D
D=M
@ARG
M=D
@R15
D=M
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@LCL
M=D
@R14
0;JMP
