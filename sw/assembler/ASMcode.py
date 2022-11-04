

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

        dest_dict = {'%A':'001','%D':'010','(%A)':'100','(%A), %A':'101','%A, (%A)':'101','(%A), %D':'110','%D, (%A)':'110','(%A), %D, %A':'111','(%A), %A, %D':'111','%A, (%A), %D':'111','%D, (%A), %A':'111','%A, %D, (%A)':'111','%D, %A, (%A)':'111','%D, %A':'011', '%A, %D':'011'}
        if mnemnonic[-1] in dest_dict:
            if mnemnonic[0] == 'movw':
                if len(mnemnonic)>3:
                    mnemnonic = [mnemnonic[0], mnemnonic[1], mnemnonic[2]+", "+mnemnonic[3]]
            return dest_dict[mnemnonic[-1]]
        return "000"

    # TODO
    def comp(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de cálculo.
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits:  Opcode (String de 7 bits) com código em linguagem de máquina para a instrução.
        """
        dict_comp = {'$0':'101010','$1':'111111','$-1':'111010','%D':'001100','%A':'110000','(%A)':'110000','!%D':"001101","!%A":"110001","!(%A)":"110001",'-%D':"001111","-%A":"110011","-(%A)":"110011",'%D+$1':"011111",'$1+%D':"011111","%A+$1":"110111","$1+%A":"110111","(%A)+$1":"110111","$1+(%A)":"110111",'%D-$1':"001110","%A-$1":"110010","(%A)-$1":"110010",'%D+%A':'000010','%D+(%A)':'000010','%D-%A':'010011','%D-(%A)':'010011','%A+%D':'000010','(%A)+%D':'000010','%A-%D':'000111','(%A)-%D':'000111','&':'000000','|':'010101'}
        # dict_n = {'notw':'!','negw':'-','incw':'+$1','decw':'-$1',}
        if mnemnonic[0][0] == 'j':
            return '0001100'
        
        else:
            n = mnemnonic[1]
            if mnemnonic[0] == 'notw':
                n = '!'+mnemnonic[1]
            elif mnemnonic[0] == 'negw':
                n = '-'+mnemnonic[1]
            elif mnemnonic[0] == 'incw':
                n = mnemnonic[1]+'+$1'
            elif mnemnonic[0] == 'decw':
                n = mnemnonic[1]+'-$1'
            elif mnemnonic[0] == 'subw':
                n = mnemnonic[1]+'-'+mnemnonic[2]
            elif mnemnonic[0] == 'rsubw':
                n = mnemnonic[2]+'-'+mnemnonic[1]
            elif mnemnonic[0] == 'addw':
                n = mnemnonic[1]+'+'+mnemnonic[2]
            elif mnemnonic[0] == 'andw':
                n = '&'
            elif mnemnonic[0] == 'orw':
                n = '|'

            if '(' in mnemnonic[1] or (len(mnemnonic)>3 and '(' in mnemnonic[2]):
                return '1'+dict_comp[n]
            return '0'+dict_comp[n]

    # TODO
    def jump(self, mnemnonic):
        """
        Retorna o código binário do mnemônico para realizar uma operação de jump (salto).
        - in mnemnonic: vetor de mnemônicos "instrução" a ser analisada.
        - return bits: (String de 3 bits) com código em linguagem de máquina para a instrução.
        """
        jump_dict = {'jg':'001','je':'010','jge':'011','jl':'100','jne':'101','jle':'110','jmp':'111'}
        if mnemnonic[0] in jump_dict:
            return jump_dict[mnemnonic[0]]
        return "000"

    # DONE
    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
