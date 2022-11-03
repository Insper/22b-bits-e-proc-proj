; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide o número posicionado na RAM[0] pelo número posicionado no RAM[1] e armazena a sobra na RAM[2].

PREPARANDO:
    leaw $3, %A
    movw $0, (%A)
WHILE:
    leaw $0, %A
    movw (%A), %D
    leaw $1, %A
    subw %D, (%A), %D


    leaw $END, %A
    jle
    nop 

    leaw $3, %A 
    movw %D, (%A)

    leaw $0, %A
    movw (%A), %D
    leaw $1, %A
    subw %D, (%A), %D
    leaw $0, %A
    movw %D, (%A)
    leaw $2, %A
    addw (%A), $1, %D
    movw %D, (%A)
    leaw $WHILE, %A
    jmp
    nop 
END:
    leaw $3, %A 
    movw (%A), %D
    leaw $2, %A 
    movw %D, (%A)