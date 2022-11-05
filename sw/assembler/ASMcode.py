

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

        bits = "000000"
        return bits

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
    def toBinary(self, value):
        """
        Converte um valor inteiro para binário 16 bits.
        """
        return f"{int(value):016b}"
