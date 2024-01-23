from produtos import Produtos

class bebidasCRUD(Produtos):
    
    lista_bebidas = []
    
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
    
    def cadastrar_bebidas(self, idd):
        nome = input("Nome: ")
        marca = input("Marca: ")
        preco = float(input("Preço: R$"))
        data_validade = input("Data validade: ")
        self.lista_bebidas.append(bebidasCRUD(idd, nome, marca, preco, data_validade))
        
    def exibir_bebidas(self):
        tamanho_lista_bebidas = len(self.lista_bebidas)
        if tamanho_lista_bebidas == 0:
            print("Nenhum alimento cadastrado!")
        else:
            for i in range(tamanho_lista_bebidas):
                data_validade_mascara = self.lista_bebidas[i].get_data_validade()
                print(f"Id: {self.lista_bebidas[i].get_idd()}\nNome: {self.lista_bebidas[i].get_nome()}\nMarca: {self.lista_bebidas[i].get_marca()}\nPreço: {self.lista_bebidas[i].get_preco()}\
                    \nData de validade: {data_validade_mascara[:2]}/{data_validade_mascara[2:4]}/{data_validade_mascara[4:8]}")
            input("\nAperte 'ENTER' para continuar: ")
                
    def editar_bebida(self):
        id_valido = False
        id_pergunta = int(input("Digite o ID: "))
        tamanho_lista_bebidas = len(self.lista_bebidas)
        for i in range(tamanho_lista_bebidas):
            if self.lista_bebidas[i].get_idd() == id_pergunta:
                id_valido = True
                print("O que deseja mudar?\n[1] - Nome\n[2] - Marca\n[3] - Preço\n[4] - Data de validade")
                try:
                    opcao = int(input("-> "))
                except:
                    print("Apenas números permitidos")
                if opcao == 1:
                    novo_dado = input("Novo nome: ")
                    self.lista_bebidas[i].set_nome(novo_dado)  #NÃO TÁ MUDANDO O VALOR, TALVEZ SEJA A HERANÇA
                elif opcao == 2:
                    novo_dado = input("Nova marca: ")
                    self.lista_bebidas[i].set_marca(novo_dado)
                elif opcao == 3:
                    novo_dado = input("Novo preço: ")
                    self.lista_bebidas[i].set_preco(novo_dado)
                elif opcao == 4:
                    novo_dado = input("Novo data de validade: ")
                    self.lista_bebidas[i].set_data_validade(novo_dado)
                else:
                    print("Opção inválida!")
                    
        if id_valido == False:
            print("ID inválido!")

    def deletar_bebida(self):
        tamanho_lista_bebidas = len(self.lista_bebidas)
        if tamanho_lista_bebidas != 0:
            id_pergunta = int(input("Digite o ID que deseja remover: "))
            for i in range(tamanho_lista_bebidas):
                if self.lista_bebidas[i].get_idd() == id_pergunta:
                    index_lista = i
                self.lista_bebidas.remove(index_lista)
        else:
            print("Nenhum alimento cadastrado!")
            
    
        
        