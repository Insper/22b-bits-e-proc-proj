; ------------------------------------
; Calcule a média dos valores de um vetor
; que possui inicio em RAM[5] e tamanho
; defindo em RAM[4],
;
; 1. Salve a soma em RAM[1]
; 2. Salve a média em RAM[0]
; 
; ------------------------------------
; antes       | depois
;             |
; RAM[0]:     | RAM[0]:  2  : média 
; RAM[1]:     | RAM[1]:  8  : soma
; RAM[2]:     | RAM[2]:  
; RAM[3]:     | RAM[3]:  
; RAM[4]:  4  | RAM[4]:  4 
; RAM[5]:  1  | RAM[5]:  1 - 
; RAM[6]:  2  | RAM[6]:  2 | vetor
; RAM[7]:  1  | RAM[7]:  1 |
; RAM[8]:  4  | RAM[8]:  4 -
; ------------------------------------

; PREP: guarda o tamanho do vetor e o inicio do vetor em ram 2 e 3

    leaw $4, %A 
    movw (%A), %D 
    leaw $2, %A 
    movw %D, (%A)

    leaw $5, %A 
    movw %A, %D
    leaw $3, %A
    movw %D, (%A)

WHILE: ;SOMA realiza a soma do vetor

    leaw $4, %A 
    subw (%A), $1, %D
    movw %D, (%A)

    leaw $3, %A 
    movw (%A), %A
    movw (%A), %D

    leaw $1, %A 
    addw %D, (%A), %D 
    movw %D, (%A)

    leaw $3, %A 
    addw (%A), $1, %D 
    movw %D, (%A)

    leaw $4, %A 
    movw (%A), %D

    leaw $WHILE, %A
    jg
    nop


; Coloca a soma em ram[3], que nao sera mais utilizada, pois e preciso subtrair
    leaw $1, %A 
    movw (%A), %D
    leaw $3, %A
    movw %D, (%A)

ENQUANTO: ;MEDIA faz a media do vetor
    leaw $3, %A 
    movw (%A), %D 

    ; Verifica se ram[3] e zero
    leaw $END, %A 
    je
    nop

    ; Como o valor de ram[2] e o tamanho do vetor (ver em PREP), usa ram[2] para subtrair de ram[3]
    leaw $2, %A 
    movw (%A), %D
    leaw $3, %A 
    subw (%A), %D, %D 
    movw %D, (%A)

    ; Verifica se o resultado dessa subtracao foi menor que zero, para evitar soma na media em caso de sobra
    leaw $END, %A 
    jl
    nop

    ; Adiciona um em ram[0], por subtracao da divisao
    leaw $0, %A 
    addw $1, (%A), %D 
    movw %D, (%A)

    ; Reseta o Loop da media
    leaw $ENQUANTO, %A 
    jmp
    nop

END:
