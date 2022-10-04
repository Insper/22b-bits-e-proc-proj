#!/usr/bin/env python3

from myhdl import *
from .components import mux2way
from .ula import inc


@block
def ram(dout, din, addr, we, clk, rst, width, depth):
    loads = [Signal(bool(0)) for i in range(depth)]
    outputs = [Signal(modbv(0)[width:]) for i in range(depth)]
    registersList = [None for i in range(depth)]

    @always_comb
    def comb():
        pass

    return instances()


@block
def pc(increment, load, i, output, width, clk, rst):
    print(increment, load, i, output, width, clk, rst)

    regIn = Signal(modbv(0)[width:])
    regOut = Signal(modbv(0)[width:])

    incOut = Signal(modbv(0)[width:])

    regLoad = Signal(bool(0))

    mux2out = Signal(modbv(0)[width:])
    mux1out = Signal(modbv(0)[width:])
    regOut = Signal(modbv(0)[width:])

    inc16 = inc(regOut, incOut)

    mux_inc = mux2way(mux1out, False, incOut, increment)

    mux_load = mux2way(mux2out, mux1out, i, load)

    mux_reset = mux2way(regIn, mux2out, 0, rst)

    @always_comb
    def comb():
        regLoad.next = increment or load or rst

    return instances()


@block
def registerN(i, load, output, width, clk, rst):
    binaryDigitList = [None for n in range(width)]
    outputs = [Signal(bool(0)) for n in range(width)]

    @always_comb
    def comb():
        pass

    return instances()


@block
def register8(i, load, output, clk, rst):
    binaryDigitList = [None for n in range(8)]
    output_n = [Signal(bool(0)) for n in range(8)]

    @always_comb
    def comb():
        pass

    return instances()


@block
def binaryDigit(i, load, output, clk, rst):
    q, d, clear, presset = [Signal(bool(0)) for i in range(4)]

    @always_comb
    def comb():
        pass

    return instances()


@block
def dff(q, d, clear, presset, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if clear:
            q.next = 0
        elif presset:
            q.next = 1
        else:
            q.next = d

    return instances()
