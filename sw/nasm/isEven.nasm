; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

PREPARANDO:
    leaw $3, %A
    movw $0, (%A)
    leaw $1, %A
    incw %D
    incw %D
    movw %D, (%A)
WHILE:
    leaw $5, %A
    movw (%A), %D
    leaw $1, %A
    subw %D, (%A), %D


    leaw $END, %A
    jle
    nop 

    leaw $3, %A 
    movw %D, (%A)

    leaw $5, %A
    movw (%A), %D
    leaw $1, %A
    subw %D, (%A), %D
    leaw $5, %A
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

IF:
    leaw $2, %A
    movw (%A), %D
    leaw $EPAR, %A
    je %D
    nop

    leaw $0, %A
    movw $0, %D
    movw %D, (%A)
    leaw $END2, %A
    jmp
    nop


EPAR:
    leaw $0, %A
    movw $1, %D
    movw %D, (%A)

END2: