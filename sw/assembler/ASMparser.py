import sys


class Parser:
    # DONE
    def __init__(self, inputFile):
        self.file = inputFile  # self.openFile()  # arquivo de leitura
        self.lineNumber = 0  # linha atual do arquivo (nao do codigo gerado)
        self.currentCommand = ""  # comando atual
        self.currentLine = ""  # linha de codigo atual
        self.CommandType = {"A": "A_COMMAND", "C": "C_COMMAND", "L": "L_COMMAND"}

    # DONE
    def openFile(self):
        try:
            return open(self.file, "r")
        except IOError:
            sys.exit("Erro: inputFile not found: {}".format(self.inputFile))

    # DONE
    def reset(self):
        self.file.seek(0)

    # DONE
    def close(self):
        self.file.close()

    # TODO
    def advanced(self):
        """
        Carrega uma instrução e avança seu apontador interno para o próxima
        linha do arquivo de entrada. Caso não haja mais linhas no arquivo de
        entrada o método retorna "Falso", senão retorna "Verdadeiro".
        @return Verdadeiro se ainda há instruções, Falso se as instruções terminaram.
        """

        # você deve varrer self.file (arquivo já aberto) até encontrar: fim de arquivo
        # ou uma nova instrucao
        # self.file
        
        linha_final = []
        for linha in self.file:
            linha = linha[0:].split()
            if linha != []:
                if linha[0] != ";":

                    self.currentLine = linha
                    notAcomment = True
                    for comando in linha:
                        
                        if notAcomment:
                            if comando[-1] == ',':
                                comando = comando[:-1]
                            if comando[0] == ';': 
                                notAcomment = False
                            else:
                                linha_final.append(comando)

                    self.currentCommand = linha_final
                    return True
        return False

    # TODO
    def commandType(self):
        """
        Retorna o tipo da instrução passada no argumento:
         - self.commandType['A'] para leaw, por exemplo leaw $1,%A
         - self.commandType['L'] para labels, por exemplo Xyz: , onde Xyz é um símbolo.
         - self.commandType['C'] para todos os outros comandos
        @param  self.currentCommand
        @return o tipo da instrução.
        """
        cmnd = self.currentCommand[0]
        if cmnd == 'leaw':
            return self.CommandType['A']
        elif cmnd[-1] == ':':
            return self.CommandType['L']
        else:
            return self.CommandType['C']


    # TODO
    def symbol(self):
        """
        Retorna o símbolo ou valor numérico da instrução passada no argumento.
        Deve ser chamado somente quando commandType() é A_COMMAND.
        @param  command instrução a ser analisada.
        @return somente o símbolo ou o valor número da instrução.
        """

        # analise o self.currentCommand
        return self.currentCommand[1][1:]

    # TODO
    def label(self):
        """
        Retorna o símbolo da instrução passada no argumento.
        Deve ser chamado somente quando commandType() é L_COMMAND.
        @param  command instrução a ser analisada.
        @return o símbolo da instrução (sem os dois pontos).
        """

        return self.currentCommand[0][0:-1]

    # DONE
    def command(self):
        return self.currentCommand

    # DONE
    def instruction(self):
        return self.currentCommand