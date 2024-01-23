import os
from cliente import Cliente
from entrada_saida import Entrada_saida
from validacao import Validacao

class ClienteCRUD:
    
    cliente_lista = []
    cpf_valido = False
    
    def cadastrar_cliente(self):
        self.cpf_valido = False
        nome = Validacao.validar_try_except("Informe seu primeiro nome: ", False, False, True)
        
        while(self.cpf_valido == False):
            cpf = input("Digite seu CPF: ")
            if Validacao.verificar_cpf_valido(cpf, self.cliente_lista):
                self.cpf_valido = True
        

        idade = Validacao.validar_try_except("Informe sua idade: ", True, False, False)
        saldo = Validacao.validar_try_except("Informe seu saldo: ", False, True, False)
        
        self.cliente_lista.append(Cliente(nome, cpf, idade, saldo))
    
    def exibir_informacoes_clientes(self):
        self.cpf_valido = False
        cpf_arrumado = ""
        while(self.cpf_valido == False):
            print("Para sair escreva: 'SAIR'")
            cpf = input("Digite o cpf: ").upper()
            if cpf == "SAIR":
                break
            else:
                tamanho_lista = len(self.cliente_lista)
                for i in range(tamanho_lista):
                    if(self.cliente_lista[i].get_cpf() == cpf):
                        os.system('cls')
                        cpf_arrumado = self.cliente_lista[i].get_cpf()
                        print(f"Nome: {self.cliente_lista[i].get_nome()}\nCPF: {cpf_arrumado[:3]}.{cpf_arrumado[3:6]}.{cpf_arrumado[6:9]}-{cpf_arrumado[9:11]}\
                            \nIdade: {self.cliente_lista[i].get_idade()}\nSaldo: R${self.cliente_lista[i].get_saldo():.2f}")
                        self.cpf_valido = True
                        Entrada_saida.continuar()
                    if self.cpf_valido == False:
                        os.system('cls')
                        print("CPF inválido!\n")
                
    def editar_informacao_cliente(self):
        self.cpf_valido = False
        editar = -1
        while(self.cpf_valido == False):
            print("Para sair escreva: 'SAIR'")
            cpf = input("Digite o cpf: ").upper()
            if cpf == "SAIR":
                break
            else:
                tamanho_lista = len(self.cliente_lista)
                for i in range(tamanho_lista):
                    if(self.cliente_lista[i].get_cpf() == cpf):
                        
                        editar = 1
                        while editar != 0:
                            os.system('cls')
                            print("O que deseja editar?\n[1] - Nome\n[2] - CPF\n[3] - Idade\n[4] - Saldo\n[0] - Sair")
                            editar = input("-> ")
                            os.system('cls')
                            match editar:
                                case "1":
                                    novo_dado = Validacao.validar_try_except("Digite o novo nome: ", False, False, True)
                                    self.cliente_lista[i].set_nome(novo_dado)
                                    print("\nNome editado com sucesso")
                                case "2":
                                    novo_dado = ""
                                    cpf_boolean = False
                                    while(cpf_boolean == False):
                                        novo_dado = input("Digite o novo CPF: ")
                                        if Validacao.verificar_cpf_valido(novo_dado, self.cliente_lista):
                                            self.cliente_lista[i].set_cpf(novo_dado)
                                            os.system('cls')
                                            cpf_boolean = True
                                            self.cpf_valido = True
                                            editar = 0
                                            print("\nCPF editado com sucesso")
                                        
                                case "3":
                                    novo_dado = Validacao.validar_try_except("Informe a nova idade: ", True, False, False)
                                    self.cliente_lista[i].set_idade(novo_dado)
                                    print("\nIdade editado com sucesso")
                                case "4":
                                    novo_dado = Validacao.validar_try_except("Informe o novo saldo: R$", False, True, False)
                                    self.cliente_lista[i].set_saldo(novo_dado)
                                    print("\nSaldo editado com sucesso")
                                case "0":
                                    break
                                case _:
                                    print("Opção incorreta!")
                            self.cpf_valido = True
                            Entrada_saida.continuar()
                            
                    if self.cpf_valido == False:
                        os.system('cls')
                        print("CPF inválido!\n")
                    
    def deletar_cliente(self):
        indice_lista = 0
        self.cpf_valido = False
        while(self.cpf_valido == False):
            os.system('cls')
            print("Para sair escreva: 'SAIR'")
            cpf = input("Digite o cpf: ").upper()
            if cpf == "SAIR":
                break
            else:
                tamanho_lista = len(self.cliente_lista)
                
                for i in range(tamanho_lista):
                    if(self.cliente_lista[i].get_cpf() == cpf):
                        indice_lista = i
                        self.cpf_valido = True    
                if self.cpf_valido == True:
                    del(self.cliente_lista[indice_lista])
                    print("Conta do cliente removida com sucesso!")
                    Entrada_saida.continuar()