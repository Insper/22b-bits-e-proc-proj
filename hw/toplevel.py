#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myhdl import *

from components import *
from ula import *


@block
def toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N):
    sw_s = [SW(i) for i in range(10)]
    key_s = [KEY(i) for i in range(10)]
    ledr_s = [Signal(bool(0)) for i in range(10)]
    saida = Signal(modbv(0)[8:])
    
    # x = Signal(intbv(1)[8:])
    # y = Signal(intbv(2)[8:])
    ula_1 = ula(1, 2, SW, ledr_s[8], ledr_s[9], saida, width=8)

    # ---------------------------------------- #
    @always_comb
    def comb():
        for i in range(len(saida)):
            LEDR[i].next = saida[i]
        LEDR[8].next = ledr_s[8]
        LEDR[9].next = ledr_s[9]

    return instances()


LEDR = Signal(intbv(0)[10:])
SW = Signal(intbv(0)[10:])
KEY = Signal(intbv(0)[4:])
HEX0 = Signal(intbv(1)[7:])
HEX1 = Signal(intbv(1)[7:])
HEX2 = Signal(intbv(1)[7:])
HEX3 = Signal(intbv(1)[7:])
HEX4 = Signal(intbv(1)[7:])
HEX5 = Signal(intbv(1)[7:])
CLOCK_50 = Signal(bool())
RESET_N = ResetSignal(0, active=0, isasync=True)

top = toplevel(LEDR, SW, KEY, HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, CLOCK_50, RESET_N)
top.convert(hdl="VHDL")