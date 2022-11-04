

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

        return '0000000'

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
