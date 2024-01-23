class Cliente:

    def __init__(self, nome, cpf, idade, saldo):
            self.__nome = nome 
            self.__cpf = cpf
            self.__idade = idade
            self.__saldo = saldo
            
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_idade(self):
        return self.__idade
    
    def get_saldo(self):
        return self.__saldo
    
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def set_idade(self, idade):
        self.__idade = idade
        
    def set_saldo(self, saldo):
        self.__saldo = saldo