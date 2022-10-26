#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path
import math


def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    return ram


def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)


def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)


def test_mult():
    ram = {0: 3, 1: 2}
    tst = {3: 6}
    assert nasm_test("mult.nasm", ram, tst)

    ram = {0: 6, 1: 6}
    tst = {3: 36}
    assert nasm_test("mult.nasm", ram, tst, 100000)


def test_mod():
    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 32, 1: 5}
    tst = {2: 2}
    assert nasm_test("mod.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 1}
    assert nasm_test("mod.nasm", ram, tst, 10000)


def test_div():
    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 4, 1: 2}
    tst = {2: 2}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 30, 1: 5}
    tst = {2: 6}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 46, 1: 5}
    tst = {2: 9}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 146}
    assert nasm_test("div.nasm", ram, tst, 10000)


def test_isEven():
    ram = {0: 3, 5: 6}
    tst = {0: 1}
    assert nasm_test("isEven.nasm", ram, tst)

    ram = {0: 2, 5: 23}
    tst = {0: 0}
    assert nasm_test("isEven.nasm", ram, tst)


def test_pow():
    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 16}
    tst = {0: 256}
    assert nasm_test("pow.nasm", ram, tst, 10000)


def test_stringLenght():
    ram = {}
    text = "oi tudo bem?"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)

    text = "o saci eh um ser muito especial"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)


def test_palindromo():
    ram = text_to_ram("ararr", 10)
    ram[0] = 2
    tst = {0: 0}
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

    ram = text_to_ram("arara", 10)
    ram[0] = 2
    tst = {0: 1}
    print(ram)
    assert nasm_test("palindromo.nasm", ram, tst, 10000)


def test_linha():
    ram = {}
    tst = {}
    nasm_test("linha.nasm", ram, tst, 10000)

def test_matriz():
    ram = {1000: 1, 1001: 2, 1003: 3, 1004: 4, 0: 3}
    tst = {0: -2}
    assert nasm_test("matrizDeterminante.nasm", ram, tst, 10000)
   



def test_factorial():
    ram = {0: 0}
    tst = {1: 1}
    assert nasm_test("factorial.nasm", ram, tst, 100000)



    ram = {0: 3}
    tst = {1: 6}
    assert nasm_test("factorial.nasm", ram, tst, 10000)

def test_teste():
    ram = {0: 3, 2: 1}
    tst = {2: 2}
    assert nasm_test("teste.nasm", ram, tst, 10000)


def test_vectorMean():
    ram = {4: 4, 5:1, 6:2, 7:1, 8:4}
    tst = {0: 2, 1:8}
    assert nasm_test("vectorMean.nasm", ram, tst, 10000)

    ram = {1:4, 5:3, 6:1, 7:1, 8:7}
    tst = {0: 3, 1:12}
    assert nasm_test("vectorMean.nasm", ram, tst, 10000)