; Arquivo: multiploDeDois.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; multiplo de dois, se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

leaw $2, %A
movw %A, %D
leaw $1, %A
movw %D, (%A)

leaw $5, %A
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

leaw $2, %A
movw (%A), %D
leaw $1, %A
andw %A, %D, %D

leaw $EPAR, %A
je
nop 

leaw $IMPAR, %A
jmp
nop

EPAR:
leaw $0, %A
movw $1, (%A)
leaw $1, %A
movw $0, (%A)
leaw $END, %A
jmp 
nop

IMPAR:
leaw $0, %A
movw $0, (%A)
leaw $1, %A
movw $1, (%A)

END:
