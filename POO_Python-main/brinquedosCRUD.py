from produtos import Produtos
from validacao import Validacao

class brinquedosCRUD(Produtos):
    
    lista_brinquedos = []
    
    def __init__(self, idd, nome, marca, preco, material):
        super().__init__(nome, marca, preco)
        
        self.__material = material
        self.__idd = idd
        
    def get_material(self):
        return self.__material
    def get_idd(self):
        return self.__idd

    def set_material(self, material):
        self.__material = material
    def set_idd(self, idd):
        self.__idd = idd

    def cadastrar_brinquedo(self, idd):
        nome = input("Nome: ")
        marca = input("Marca: ")
        preco = float(input("Preço: R$"))
        material = input("Material utilizado: ")
        self.lista_brinquedos.append(brinquedosCRUD(idd, nome, marca, preco, material))
        
    def exibir_brinquedos(self):
        tamanho_lista_brinquedos = len(self.lista_brinquedos)
        if tamanho_lista_brinquedos == 0:
            print("Nenhum brinquedo cadastrado!")
        else:
            for i in range(tamanho_lista_brinquedos):
                print(f"Id: {self.lista_brinquedos[i].get_idd()}\nNome: {self.lista_brinquedos[i].get_nome()}\nMarca: {self.lista_brinquedos[i].get_marca()}\nPreço: {self.lista_brinquedos[i].get_preco()}\
                    \nMaterial: {self.lista_brinquedos[i].get_material()}")
            input("\nAperte 'ENTER' para continuar: ")
                
    def editar_brinquedos(self):
        id_valido = False
        id_pergunta = Validacao.validar_try_except("Digite o ID: ", True, False, False)
        tamanho_lista_brinquedos = len(self.lista_brinquedos)
        for i in range(tamanho_lista_brinquedos):
            if self.lista_brinquedos[i].get_idd() == id_pergunta:
                id_valido = True
                print("O que deseja mudar?\n[1] - Nome\n[2] - Marca\n[3] - Preço\n[4] - Material")
                try:
                    opcao = input("-> ")
                except:
                    print("Apenas números permitidos")
                if opcao == "1":
                    novo_dado = input("Novo nome: ")
                    self.lista_brinquedos[i].set_nome(novo_dado)
                elif opcao == "2":
                    novo_dado = input("Nova marca: ")
                    self.lista_brinquedos[i].set_marca(novo_dado)
                elif opcao == "3":
                    novo_dado = input("Novo preço: ")
                    self.lista_brinquedos[i].set_preco(novo_dado)
                elif opcao == "4":
                    novo_dado = input("Novo material: ")
                    self.lista_brinquedos[i].set_material(novo_dado)
                else:
                    print("Opção inválida!")
                    
        if id_valido == False:
            print("ID inválido!")

    def deletar_brinquedo(self):
        tamanho_lista_brinquedos = len(self.lista_brinquedos)
        if tamanho_lista_brinquedos != 0:
            id_pergunta = Validacao.validar_try_except("Digite o ID que deseja remover: ", True, False, False)
            for i in range(tamanho_lista_brinquedos):
                if self.lista_brinquedos[i].get_idd() == id_pergunta:
                    index_lista = i
                self.lista_brinquedos.remove(index_lista)
        else:
            print("Nenhum brinquedo cadastrado!")
            
    
        
        