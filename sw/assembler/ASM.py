from .ASMsymbolTable import SymbolTable
from .ASMcode import Code
from .ASMparser import Parser


class ASM:

    # DONE
    def __init__(self, nasm, hack):
        self.hack = hack
        self.symbolTable = SymbolTable()
        self.parser = Parser(nasm)
        self.code = Code()
        self.hackLineCount = 0

    # DONE
    def run(self):
        try:
            self.fillSymbolTable()
            self.generateMachineCode()
            return 0
        except:
            print("--> ERRO AO TRADUZIR: {}".format(self.parser.currentLine))
            return -1

    # TODO
    def fillSymbolTable(self):
        """
        primeiro passo para a construção da tabela de símbolos de marcadores (labels)
        varre o código em busca de novos Labels e Endereços de memórias (variáveis)
        e atualiza a tabela de símbolos com os endereços (table).

        Dependencia : Parser, SymbolTable
        """
        self.hackLineCount = 0
        for lines in self.parser.file:
            while self.parser.advanced():
                if self.parser.commandType() == 'L_COMMAND':
                    if not self.symbolTable.contains(self.parser.label()):
                        self.symbolTable.addEntry(self.parser.label(), self.hackLineCount)
                else:
                    self.hackLineCount += 1


    # TODO
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code
        """

        while self.parser.advanced():
            if self.parser.commandType() == "C_COMMAND":
                bin = '0x' + self.code.toBinary(self.hack[1])
                self.hack.write(bin + "\n")

            elif self.parser.commandType() == "A_COMMAND":
                bin = "0x1000" + self.code.comp(self.hack)+'0'+self.code.dest(self.hack)+self.code.jump(self.hack)
                self.hack.write(bin + "\n")
                
        self.hack.close()