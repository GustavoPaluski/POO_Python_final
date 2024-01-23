from produtos import Produtos
from validacao import Validacao

class Alimentos(Produtos):
    
    lista_alimentos = []
    
    def __init__(self, idd, nome, marca, preco, data_validade):
        super().__init__(nome, marca, preco)
        
        self.__idd = idd
        self.__data_validade = data_validade
        
    def get_data_validade(self):
        return self.__data_validade
    def get_idd(self):
        return self.__idd
    
    def set_data_validade(self, data_validade):
        self.__data_validade = data_validade
    def set_id(self, idd):
        self.__idd = idd
    
    def cadastrar_alimento(self, idd):
        nome = Validacao.validar_try_except("(Somente Letras) Nome: ", False, False, True)
        marca = Validacao.validar_try_except("(Somente Letras) Marca: ", False, False, True)
        preco = Validacao.validar_try_except("Preço: R$", False, True, False)
        data_validade = Validacao.validar_data_validade()
        self.lista_alimentos.append(Alimentos(idd, nome, marca, preco, data_validade))
        
    def exibir_alimentos(self):
        tamanho_lista_alimentos = len(self.lista_alimentos)
        if tamanho_lista_alimentos == 0:
            print("Nenhum alimento cadastrado!")
        else:
            for i in range(tamanho_lista_alimentos):
                data_validade_mascara = self.lista_alimentos[i].get_data_validade()
                print(f"Id: {self.lista_alimentos[i].get_idd()}\nNome: {self.lista_alimentos[i].get_nome()}\nMarca: {self.lista_alimentos[i].get_marca()}\nPreço: {self.lista_alimentos[i].get_preco()}\
                    \nData de validade: {data_validade_mascara[:2]}/{data_validade_mascara[2:4]}/{data_validade_mascara[4:8]}")
            input("\nAperte 'ENTER' para continuar: ")
                
    def editar_alimento(self):
        id_valido = False
        id_pergunta = Validacao.validar_try_except("Digite o ID: ", True, False, False)
        tamanho_lista_alimentos = len(self.lista_alimentos)
        for i in range(tamanho_lista_alimentos):
            if self.lista_alimentos[i].get_idd() == id_pergunta:
                id_valido = True
                print("O que deseja mudar?\n[1] - Nome\n[2] - Marca\n[3] - Preço\n[4] - Data de validade")
                try:
                    opcao = input("-> ")
                except:
                    print("Apenas números permitidos")
                if opcao == "1":
                    novo_dado = Validacao.validar_try_except("(Somente Letras) Novo nome: ", False, False, True)
                    self.lista_alimentos[i].set_nome(novo_dado)  #NÃO TÁ MUDANDO O VALOR, TALVEZ SEJA A HERANÇA
                elif opcao == "2":
                    novo_dado = Validacao.validar_try_except("(Somente Letras) Nova marca: ", False, False, True)
                    self.lista_alimentos[i].set_marca(novo_dado)
                elif opcao == "3":
                    novo_dado = Validacao.validar_try_except("Novo preço: ", False, True, False)
                    self.lista_alimentos[i].set_preco(novo_dado)
                elif opcao == "4":
                    novo_dado = Validacao.validar_data_validade()
                    self.lista_alimentos[i].set_data_validade(novo_dado)
                else:
                    print("Opção inválida!")
                    
        if id_valido == False:
            print("ID inválido!")

    def deletar_alimento(self):
        tamanho_lista_alimentos = len(self.lista_alimentos)
        if tamanho_lista_alimentos != 0:
            id_pergunta = int(input("Digite o ID que deseja remover: "))
            for i in range(tamanho_lista_alimentos):
                if self.lista_alimentos[i].get_idd() == id_pergunta:
                    index_lista = i
                self.lista_alimentos.remove(index_lista)
        else:
            print("Nenhum alimento cadastrado!")
            
    
        
        