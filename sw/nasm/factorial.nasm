; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.


PREPARANDO:
    leaw $3, %A
    movw $0, (%A)
    leaw $0, %A
    movw (%A), %D
    leaw $1, %A
    movw %D, (%A)
    subw (%A), $1, %D
    leaw $FIM1, %A
    jle
    nop
    leaw $1, %A
    movw %D, (%A)
WHILE:
    leaw $0, %A
    movw (%A), %D
    leaw $END, %A
    je 
    nop 

    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    addw (%A), %D, %D
    movw %D, (%A)
    leaw $0, %A
    subw (%A), $1, %D
    movw %D, (%A)
    leaw $WHILE, %A
    jmp
    nop 
END:
    leaw $3, %A
    movw (%A), %D
    leaw $0, %A
    movw %D, (%A)
    leaw $1, %A
    subw (%A), $1, %D
    leaw $1, %A
    movw %D, (%A)
    leaw $FIM, %A
    je
    nop
    leaw $WHILE, %A
    jmp
    nop 

FIM:
    leaw $3, %A
    movw (%A), %D
    leaw $1, %A
    movw %D, (%A)
    leaw $FIM2, %A
    jmp
    nop

FIM1:
    leaw $1, %A
    movw %A, %D
    leaw $1, %A
    movw %D, (%A)


FIM2:



