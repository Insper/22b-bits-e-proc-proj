#!/usr/bin/env python3

from myhdl import *


@block
def and16(a, b, q):
    """
    a: 16 bits
    b: 16 bits
    q: 16 bits

    and bit a bit entre a e b
    """
    foo = Signal(0)

    @always_comb
    def comb():
        q.next = (a and b)

    return comb


@block
def or8way(a, b, c, d, e, f, g, h, q):
    """
    a, b, c, ... h: 1 bit

    or bit a bit entre a e b
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        q.next = (a or b or c or d or e or f or g or h)

    return comb


@block
def orNway(a, q):
    """
    a: 16 bits
    q: 1 bit

    or bit a bit dos valores de a: a[0] or a[1] ...
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        final = a[0]
        for value in a:
            if value:
                final = value
        q.next = final

    return comb


@block
def barrelShifter(a, dir, size, q):
    """
    a: 16 bits
    dir: 1 bit
    size: n bits
    q: 16 bits

    se dir for 0, shifta para direita `size`
    se dir for 1, shifta para esquerda `size`

    exemplo: a = 0000 1111 0101 1010, dir = 0, size = 3
             q = 0111 1010 1101 0000
    """

    @always_comb
    def comb():
        q.next = q.next = a >> size if not dir else a << size #ideia retirada de https://stackoverflow.com/questions/22832615/what-do-and-mean-in-python

    return comb


@block
def mux2way(q, a, b, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    sel: 2 bits

    Mux entre a e b, sel é o seletor
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        if sel == 0:
            q.next = a 
        elif sel == 1:
            q.next = b
    return comb


@block
def mux4way(q, a, b, c, d, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    c: 16 bits
    d: 16 bits
    sel: 4 bits

    Mux entre a, b, c, d sel é o seletor
    """
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        lista = [a,b,c,d]
        q.next = lista[sel]

    return comb


@block
def mux8way(q, a, b, c, d, e, f, g, h, sel):
    """
    Mux de 8 entradas, simular aos anteriores.
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        lista = [a,b,c,d,e,f,g,h]
        q.next = lista[sel]

    return comb


@block
def deMux2way(a, q0, q1, sel):
    """
    deMux de 2 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0

    Exemplo:

    a = 0xFFAA, sel = 0
    q0 = 0xFFAA
    q1 = 0
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        if sel == 1:
            q1.next = a
            q0.next = 0
        else:
            q0.next = a
            q1.next = 0 
        
    return comb


@block
def deMux4way(a, q0, q1, q2, q3, sel):
    """
    deMux de 4 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        q0.next = 0
        q1.next = 0 
        q2.next = 0
        q3.next = 0
        if sel == 0:
            q0.next = a
        if sel == 1:
            q1.next = a
        if sel == 2:
            q2.next = a
        if sel == 3: 
            q3.next = a
    return comb


@block
def deMux8way(a, q0, q1, q2, q3, q4, q5, q6, q7, sel):
    """
    deMux de 8 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0
    """

    @always_comb
    def comb():
        q0.next = 0
        q1.next = 0 
        q2.next = 0
        q3.next = 0
        q4.next = 0
        q5.next = 0
        q6.next = 0
        q7.next = 0
        if sel == 0:
            q0.next = a
        if sel == 1:
            q1.next = a
        if sel == 2:
            q2.next = a
        if sel == 3: 
            q3.next = a
        if sel == 4:
            q4.next = a
        if sel == 5:
            q5.next = a
        if sel == 6:
            q6.next = a
        if sel == 7:
            q7.next = a
    return comb


# -----------------------------#
# Conceito B
# -----------------------------#
#
@block
def bin2hex(hex0, sw):
    """
    importar do lab!
    """

    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex0.next = "1000000"
        elif sw[4:0] == 1:
            hex0.next = "1111001"
        elif sw[4:0] == 2:
            hex0.next = "0100100"
        elif sw[4:0] == 3:
            hex0.next = "0110000"
        elif sw[4:0] == 4:
            hex0.next = "0011001"
        elif sw[4:0] == 5:
            hex0.next = "0010010"
        elif sw[4:0] == 6:
            hex0.next = "0000010"
        elif sw[4:0] == 7:
            hex0.next = "1111000"
        elif sw[4:0] == 8:
            hex0.next = "0000000"
        elif sw[4:0] == 9:
            hex0.next = "0010000"
    return instances()


DIG1 = tuple(i for i in range(10) for _ in range(10)) 
DIG0 = tuple(i for i in range(10) for i in range(10))
@block
def bin2bcd(b, bcd1, bcd0):
    """
    componente que converte um vetor de b[8:] (bin)
    para dois digitos em BCD

    Exemplo:
    bin  = `01010010`
    BCD1 = 8
    BCD0 = 2
    """
    
    @always_comb
    def comb():
        bcd0.next = DIG1[int(b)]
        bcd1.next = DIG0[int(b)]
    return instances()


# -----------------------------#
# Conceito A
# -----------------------------#
