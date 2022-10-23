; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

;SETUP

    leaw $2, %A
    movw %A, %D
    movw %D, (%A)

WHILE:

    leaw $5, %A
    movw (%A), %D

    leaw $2, %A
    subw %D, (%A), %D 
    leaw $5, %A
    movw %D, (%A)

    leaw $AN, %A
    jle
    nop

    leaw $WHILE, %A
    jmp
    nop

AN:
    leaw $ENDIMPAR, %A
    jl
    nop

    leaw $ENDPAR, %A
    je 
    nop

ENDIMPAR:
    leaw $0, %A 
    movw $0, (%A)

    leaw $END, %A 
    jmp 
    nop

ENDPAR:
    leaw $0, %A 
    movw $1, (%A)

END:
