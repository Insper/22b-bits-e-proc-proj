; Arquivo: LCDQuadrado.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
; Data: 28/3/2018
;
; Desenhe um quadro no LCD

leaw $16, %A
movw %A, %D
leaw $0, %A 
movw %D, (%A)

leaw $16385, %A
movw %A, %D
leaw $1, %A 
movw %D, (%A)
    
leaw $1, %A 
movw (%A), %A
movw $0, %D            
notw %D
movw %D, (%A)

WHILE:

    leaw $1, %A
    movw (%A), %D
    leaw $20, %A
    addw %D, %A, %D  
    leaw $1, %A
    movw %D, (%A)

    leaw $0, %A
    movw (%A), %D
    subw %D, $1, %D 
    movw %D, (%A)

    leaw $END, $A
    je               
    nop 

    leaw $32769, %A
    movw %A, %D
    leaw $1, %A
    movw (%A), %A
    movw %D, (%A)

    leaw $WHILE, %A
    jmp
    nop

END:

    leaw $1, %A 
    movw (%A), %A
    movw $0, %D           
    notw %D
    movw %D, (%A)
