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
        q.next = foo
 
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
        q.next = foo
 
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
        q.next = foo
 
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
        q.next = foo
 
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
        q.next = foo
 
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
        q.next = foo
 
    return comb
 
 
@block
def mux8way(q, a, b, c, d, e, f, g, h, sel):
    """
    Mux de 8 entradas, simular aos anteriores.
    """
 
    foo = Signal(intbv(0))
 
    @always_comb
    def comb():
        q.next = foo
 
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
       lista = [a,b]
       q.next = lista[sel]
 
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
def deMux8way(a, q0, q1, q2, q3, q4, q5, q6, q7, sel):
    """
    deMux de 8 saídas e uma entrada.
 
    - Lembre que a saída que não está ativada é 0
    """
 
    foo = Signal(intbv(0))
 
    @always_comb
    def comb():
        q0.next = foo
 
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
 
DIG0 = tuple(i for i in range(10) for i in range(10))
DIG1 = tuple(i for i in range(10) for _ in range(10))

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
        bcd0.next = DIG0[int(b)]
        bcd1.next = DIG1[int(b)]

 
    return comb
 
 
# -----------------------------#
# Conceito A
# -----------------------------#