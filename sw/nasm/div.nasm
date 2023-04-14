; Arquivo: Div.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Divide R0 por R1 e armazena o resultado em R2.
; (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
; divisao para numeros inteiros positivos

leaw $0, %A
movw (%A), %D
leaw $3, %A
movw %D, (%A)

WHILE:

    leaw $2, %A
    addw (%A), $1, %D
    movw %D, (%A)

    leaw $1, %A
    movw (%A), %D
    leaw $3, %A
    subw (%A), %D, %D

    leaw $END, %A
    jle %D
    nop

    leaw $3, %A
    movw %D, (%A)

    leaw $WHILE, %A
    jmp nop

END:

leaw $FIM, %A
je %D
nop

leaw $2, %A
subw (%A), $1, %D
movw %D, (%A)

FIM: