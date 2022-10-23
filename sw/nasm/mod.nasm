; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide o número posicionado na RAM[0] pelo número posicionado no RAM[1] e armazena a sobra na RAM[2].
;SETUP
    leaw $0, %A
    movw (%A), %D

WHILE:
    leaw $MENOR, %A 
    jl
    nop

    leaw $IGUAL, %A
    je
    nop

    leaw $1, %A 
    subw %D, (%A), %D

    leaw $WHILE, %A 
    jmp
    nop

MENOR:
    leaw $1, %A 
    addw %D, (%A), %D 

IGUAL:
    leaw $2, %A
    movw %D, (%A)
    