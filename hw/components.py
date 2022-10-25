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

    @always_comb
    def comb():
        q.next = a and b

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
        q.next = a or b or c or d or e or f or g or h

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
        q.next = a[0] or a[1]

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
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        if dir == 0:
            q.next = a >> size
        else:
            q.next = a << size
    return comb


@block
def mux2way(q, a, b, sel):
    """
    q: 16 bits
    a: 16 bits
    b: 16 bits
    sel: 2 bits

    Mux entre a e b, sel é o seletor"""
    foo = Signal(intbv(0))

    @always_comb
    def comb():
        entradas = [a,b]
        q.next = entradas[sel]

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
        sel2= str(sel)
        print(sel2)
        if sel2 == "0":
            q.next = a
        
        if sel2 == "1":
            q.next = b
        
        if sel2 == "2":
            q.next = c
        
        if sel2 == "3":
            q.next = d
       
        

    return comb


@block
def mux8way(q, a, b, c, d, e, f, g, h, sel):
    """
    Mux de 8 entradas, simular aos anteriores.
    """

    foo = Signal(intbv(0))

    @always_comb
    def comb():
        
        entradas = [a,b,c,d,e,f,g,h]
        q.next = entradas[sel]
        # q.next = foo

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
        lista_entradas = [q0,q1]
        for num in range(0, len(lista_entradas)):
            if num == sel:
                lista_entradas[num].next = a
            else: 
                lista_entradas[num].next = 0

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
        saidas = [q0, q1, q2, q3]
        for index in range(0, len(saidas)):
            if index == sel:
                saidas[index].next = a
            else:
                saidas[index].next = 0

    return comb


@block
def deMux8way(a, q0, q1, q2, q3, q4, q5, q6, q7, sel):
    """
    deMux de 8 saídas e uma entrada.

    - Lembre que a saída que não está ativada é 0
    """

    foo = Signal(intbv(0))


    @always_comb
    def comb():

        saidas = [q0,q1,q2,q3,q4,q5,q6,q7]
        for i in range(7):
            if sel == i:
                saidas[i].next = a
            else :
                saidas[i].next = 0

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
        hex0.next[4:] = sw[4:]

    return comb


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

    foo = Signal(intbv(0)[4:])

    @always_comb
    def comb():
        bcd1.next = foo
        bcd0.next = foo

    return comb


# -----------------------------#
# Conceito A
# -----------------------------#
