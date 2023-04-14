; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe uma linha no LCD

INICIO: ; 
    leaw $20, %A 
    movw %A, %D
    leaw $0, %A
    movw %D, (%A) 

    leaw $16384, %A
    movw %A, %D
    leaw $1, %A
    movw %D, (%A)
    
LOOP: 
    leaw $1, %A
    movw (%A), %D
    movw %D, %A
    movw $0, %D
    notw %D
    movw %D, (%A)

    leaw $0, %A
    movw (%A), %D
    subw %D, 1, %D
    movw %D, (%A)

    leaw $END, %A
    je
    nop

    leaw $1, %A
    movw (%A), %D
    addw 1, %D, %D
    movw %D, (%A)

    leaw $LOOP, %A
    jmp
    nop