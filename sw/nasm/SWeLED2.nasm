; Arquivo: SWeLED2.nasm
; Curso: Elementos de Sistemas
; Criado por: Rafael Corsi
;
; Faça os LEDs exibirem 
; LED = SW[8] !SW[7] OFF ON ON RAM[5][3] ON SW[0] OFF 
;                                ^            ^
;                                | TRUQUE!    | TRUQUE!
; 

leaw $52, %A
movw %A, %D
leaw $0, %A
movw %D, (%A)

SW8:
leaw $21185, %A
movw (%A), %D
leaw $256, %A
andw %D, %A, %D

leaw $SW7, %A
je
nop

leaw $0, %A 
movw (%A), %D
leaw $256, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)

SW7:
leaw $21185, %A
movw (%A), %D
leaw $128, %A
andw %D, %A, %D

leaw $RAM5, %A
jg
nop

leaw $0, %A 
movw (%A), %D
leaw $128, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)

RAM53:
leaw $5, %A
movw (%A), %D
leaw $8, %A
andw %D, %A, %D

leaw $SW0, %A
je
nop

leaw $0, %A 
movw (%A), %D
leaw $8, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)


SW0:
leaw $21185, %A
movw (%A), %D
leaw $1, %A
andw %D, %A, %D

leaw $END, %A
je
nop

leaw $0, %A 
movw (%A), %D
leaw $2, %A
addw %D, %A, %D
leaw $0, %A
movw %D, (%A)

END:
leaw $0, %A
movw (%A), %D
leaw $21184, %A
movw %D, (%A)