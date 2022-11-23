; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe uma linha no LCD


leaw $18784, %A
movw %A, %D
leaw $0, %A 
movw %D, (%A)
leaw $20, %A 
movw %A, %D
leaw $1, %A 
movw %D, (%A)
WHILE:
    leaw $0, %A
    movw (%A), %D 
    movw %D, %A
    movw $-1, (%A)
    leaw $0, %A
    movw (%A), %D
    incw %D 
    movw %D, (%A)
    leaw $1, %A
    subw (%A), $1, %D
    movw %D, (%A)
    leaw $WHILE, %A
    jg
    nop