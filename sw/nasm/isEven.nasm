; Arquivo: isEven.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2019
;
; Verifica se o valor salvo no endereço RAM[5] é
; par. Se for verdadeiro, salva 1
; em RAM[0] e 0 caso contrário.

PREPARANDO:
    leaw $0, %A
    movw %A, %D
    movw %D, (%A)
    movw (%A), %D       
    leaw $5, %A
    movw (%A), %D
    leaw $PAR, %A
    je 
    nop 

WHILE:
    leaw $2, %A
    subw %D, %A, %D
    leaw $PAR, %A
    je
    nop
    leaw $IMPAR, %A
    jl
    nop
    leaw $WHILE, %A
    jmp
    nop

IMPAR:
    leaw $0, %A
    movw %A, %D
    leaw $0, %A
    movw %D, (%A)
    leaw $END, %A
    jmp
    nop
    

PAR:
    leaw $1, %A
    movw %A, %D
    leaw $0, %A
    movw %D, (%A)

END:
