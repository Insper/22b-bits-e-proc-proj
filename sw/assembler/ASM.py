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
        self.parser.reset()
        dict_entradas = {}
        contador = 0
        while self.parser.advanced() == True:
            if ':' in self.parser.command()[0]:
                contador += 1

                dict_entradas[self.parser.command()[0][:-1]] = self.parser.currentLine - contador

        for key,value in dict_entradas.items():
            self.symbolTable.addEntry(key,value)
        


    # TODO
    def generateMachineCode(self):
        """
        Segundo passo para a geração do código de máquina
        Varre o código em busca de instruções do tipo A, C
        gerando a linguagem de máquina a partir do parse das instruções.

        Dependencias : Parser, Code, fillSymbolTable
        """
        bin = ''
        self.parser.lineNumber = 0
        self.parser.currentCommand = ''
        self.parser.file=open('test_assets/factorial.nasm', 'r')

        while self.parser.advanced():
            
            comando_atual = self.parser.currentCommand
            if self.parser.commandType() == "L_COMMAND":
                pass

            elif self.parser.commandType() == "C_COMMAND":

                if comando_atual[0][0] == "j" :

                    bin = "100000011000000"+self.code.jump(comando_atual)

                elif comando_atual[0] == 'nop':

                    bin = '100001010100000000'

                else :
                    bin = '1000'+self.code.comp(comando_atual)+'0'+self.code.dest(comando_atual)+self.code.jump(comando_atual)

                self.hack.write(bin + "\n")
                

            elif self.parser.commandType() == "A_COMMAND":

                endereco = self.symbolTable.getAddress(self.parser.symbol())
                if endereco == None :
                    bin = "00"+self.code.toBinary(self.parser.symbol())
                else :
                    bin = "00"+self.code.toBinary(endereco)

                self.hack.write(bin + "\n")
