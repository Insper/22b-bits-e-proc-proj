; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.

; 0 -> spot with number to be used
; 1 -> result
; 2 -> counter for factorial
; 3 -> current multiplication number
; 4 -> counter for multiplications

Preparando:
    leaw $0, %A     ; gets ram0 memory to %D
    movw (%A), %D
    leaw $1, %A     ; clears ram memory
    movw $1, (%A)

    leaw $2, %A     ; makes ram2 = ram1
    movw %D, (%A)

    leaw $3, %A     ; clears ram memory
    movw $0, (%A)
    leaw $4, %A     ; clears ram memory
    movw $0, (%A)


FACTORIAL:

    leaw $2, %A         ; subtracts factorial counter
    subw (%A), $1, %D
    movw %D, (%A)      

    leaw $1, %A         ; result to current number
    movw (%A), %D
    leaw $3, %A
    movw %D, (%A)

    leaw $2, %A         ; factorial counter copy to multiplication counter
    movw (%A), %D
    leaw $4, %A         
    movw %D, (%A)

    leaw $2, %A         ; checks if counter is <= 1    
    leaw $FINAL, %A       
    jle %D
    nop    

    leaw $WHILE, %A     ; factorial loop (going to while)
    jmp
    nop


WHILE:
    leaw $4, %A         ; checks if multiplication counter is 0
    movw (%A), %D
    leaw $FACTORIAL, %A
    je %D
    nop

    leaw $3, %A         ; adds second numb to first
    movw (%A), %D
    leaw $1, %A
    addw (%A), %D, %D
    movw %D, (%A)

    leaw $4, %A         ; subtracts multiplication counter 
    subw (%A), $1, %D
    movw %D, (%A)

    leaw $WHILE, %A     ; while loop
    jmp
    nop

END:
    