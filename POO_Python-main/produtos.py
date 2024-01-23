class Produtos:
    
    def __init__(self, nome, marca, preco):
        
        self.__nome = nome
        self.__marca = marca
        self.__preco = preco
        
    def get_nome(self):
        return self.__nome
    
    def get_marca(self):
        return self.__marca
    
    def get_preco(self):
        return self.__preco
    
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_marca(self, marca):
        self.__marca = marca

    def set_preco(self, preco):
        self.__preco = preco
        
    