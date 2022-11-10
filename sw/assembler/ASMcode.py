


from operator import le

class Code:
    def __init__(self):
        """
        Se precisar faca uso de variáveis.
        """
        pass

    # TODO
    def dest(self, mnemnonic):
        """
        Retorna o código binário do(s) registrador(es) que vão receber o valor da instrução.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: String de 4 bits com código em linguagem de máquina
          que define o endereco da operacao
        """

        if len(mnemnonic) == 1:
            bits = '000'
        elif len(mnemnonic) == 2:
            if mnemnonic[-1] == "%A":
                bits = '001'
            elif mnemnonic[-1] == "(%A)":
                bits = '100'
            elif mnemnonic[-1] == "%D":
                bits = '010'
            else : 
                bits = '000'
        elif len(mnemnonic) == 3:
            if mnemnonic[-1] == "%D" :
                bits = '010'
            elif mnemnonic[-1] == "%A" :
                bits = '001'
            elif mnemnonic[-1] == "(%A)" :
                bits = '100'
        elif len(mnemnonic) == 4:
            if mnemnonic[-1] == "%D" :
                bits = '010'
            elif mnemnonic[-1] == "%A" :
                bits = '001'
            elif mnemnonic[-1] == "(%A)" :
                bits = '100'

        else : 
            if mnemnonic[-2] == '%D' and mnemnonic[-1] == '(%A)' :
                bits = '110'
            elif mnemnonic[-2] == '%D' and mnemnonic[-1] == '%D' :
                bits = '010'
            elif mnemnonic[-2] == '(%A)' and mnemnonic[-1] == '%A' :
                bits = '001'
            elif mnemnonic[-2] == '%A' and mnemnonic[-1] == '%A' :
                bits = '001'
            else:
                bits = "000"
        return bits

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """
        mnemnonic2 = ''
        for a in mnemnonic :
            mnemnonic2 += a

        gamb = {'subw%D$1(%A)':'1001110','movw$0(%A)':'0101010','movw%A%D': '0110000', 'movw%D%A': '0001100', 'movw%D(%A)': '0001100', 'movw(%A)%A': '1110000', 'movw%A(%A)': '0110000', 'movw$1%D': '0111111', 'addw%A%D%D': '0000010', 'addw(%A)%D%D': '1000010', 'addw$1(%A)%D': '1110111', 'incw%A': '0110111', 'incw%D': '0011111', 'incw(%A)': '1110111', 'movw(%A)%D': '1110000', 'subw%D(%A)%A': '1010011', 'rsubw%D(%A)%A': '1000111',
                'decw%A': '0110010', 'decw%D': '0001110', 'notw%A': '0110001', 'notw%D': '0001101', 'negw%A': '0110011', 'negw%D': '0001111', 'andw(%A)%D%D': '1000000', 'andw%D%A%A': '0000000', 'orw(%A)%D%D': '1010101', 'orw%D%A%A': '0010101', 'subw(%A)$1%A': '1110010', 'jmp': '0001100', 'je': '0001100', 'jne': '0001100', 'jg': '0001100', 'jge': '0001100', 'jl': '0001100', 'jle': '0001100'}

        return gamb[mnemnonic2]


    # TODO
    def jump(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de jump (salto).
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: (String de 3 bits) com código em linguagem de máquina para a instrução.
        """

        dict_jumps = {
            'jmp' : '111', 
            'je' : '010', 
            'jne' : '101', 
            'jg' : '001', 
            'jge' : '011', 
            'jl' : '100', 
            'jle' : '110'
        }
        if mnemnonic[0] in dict_jumps.keys() :
            bits = dict_jumps[mnemnonic[0]]
        else :
            bits = "000"
        return bits

    # DONE
        if len(mnemnonic) == 1:
            mnemnonicTeste = mnemnonic[0]
            jumps = {"jmp": "111",
                     "je": "010",
                     "jne": "101",
                     "jg": "001",
                     "jge": "011",
                     "jl": "100",
                     "jle": "110",
                     "nop": "000"
                     }

            return jumps[mnemnonicTeste]

        else:
            return "000"


    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
