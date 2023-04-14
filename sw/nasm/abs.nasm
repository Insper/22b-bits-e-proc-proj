; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Copia o valor de RAM[1] para RAM[0] deixando o valor sempre positivo.

leaw $1, %A ; A = 1
movw (%A), %D ; D = RAM[1]
leaw $ABS, %A ; A = ABS
jl %D ; Se D < 0, pula para ABS
nop
leaw $0, %A ; A = 0 
movw %D, (%A) ; RAM[0] = RAM[1]
leaw $END, %A 
jmp 
nop

ABS:
    negw %D ; D = -D 
    leaw $0, %A ; A = 0 
    movw %D, (%A) ; RAM[0] = RAM[1]
    
END: