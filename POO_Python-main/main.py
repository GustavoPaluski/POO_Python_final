import os
from cliente import Cliente
from clienteCRUD import ClienteCRUD
from entrada_saida import Entrada_saida
from alimentosCRUD import Alimentos
from bebidasCRUD import bebidasCRUD
from brinquedosCRUD import brinquedosCRUD

class main:
    
    cliente_crud = ClienteCRUD()
    alimentos = Alimentos(0, "", "", 0.0, "")
    bebidas_crud = bebidasCRUD(0, "", "", 0.0, "")
    contador_id = 0
    brinquedos_crud = brinquedosCRUD(0, "", "", 0.0, "")
    
    while(True):
        os.system('cls')
        print("     __  __ ______ _____   _____         _____ _____ _   _ _    _  ____  ")
        print("    |  \/  |  ____|  __ \ / ____|  /\   |  __ \_   _| \ | | |  | |/ __ \ ")
        print("    | \  / | |__  | |__) | |      /  \  | |  | || | |  \| | |__| | |  | |")
        print("    | |\/| |  __| |  _  /| |     / /\ \ | |  | || | | . ` |  __  | |  | |")
        print("    | |  | | |____| | \ \| |____/ ____ \| |__| || |_| |\  | |  | | |__| |")
        print("    |_|  |_|______|_|  \_\\_____/_/    \_\_____/_____|_| \_|_|  |_|\____/ \n\n")
        opcao = Entrada_saida.menu_principal()
        
        match opcao:
            case "1":
                opcao_cliente = " "
                while(opcao_cliente != "0"):
                    os.system('cls')
                    opcao_cliente = Entrada_saida.menu_cliente()
                    os.system('cls')
                    match opcao_cliente:   
                        case "1":
                            os.system('cls')
                            cliente_crud.cadastrar_cliente()
                        case "2":
                            os.system('cls')    
                            cliente_crud.exibir_informacoes_clientes()
                        case "3":
                            os.system('cls')
                            cliente_crud.editar_informacao_cliente()
                        case "4":
                            cliente_crud.deletar_cliente()
                            os.system('cls')
                        case "0":
                            break
                        case _:
                            os.system('cls')
                            print("Opção inválida!")
            case "2":
                opcao_alimento = " "
                while(opcao_alimento != "0"):
                    os.system('cls')
                    opcao_alimento = Entrada_saida.menu_alimentos()
                    os.system('cls')
                    match opcao_alimento:
                        case "1":
                            os.system('cls')
                            contador_id += 1
                            idd = contador_id
                            alimentos.cadastrar_alimento(idd)
                        case "2":
                            os.system('cls')
                            alimentos.exibir_alimentos()
                        case "3":
                            os.system('cls')
                            alimentos.editar_alimento()
                            input("Continuar ")
                        case "4":
                            os.system('cls')
                            alimentos.deletar_alimento()
                        case "0":
                            break          
                        case _:
                            os.system('cls')
                            print("Opção inválida!")
                            Entrada_saida.continuar()

            case "3":
                opcao_bebidas = " "
                while(opcao_bebidas != "0"):
                    os.system('cls')
                    opcao_bebidas = Entrada_saida.menu_bebidas()
                    os.system('cls')
                    match opcao_bebidas:
                        case "1":
                            os.system('cls')
                            contador_id += 1
                            idd = contador_id
                            bebidas_crud.cadastrar_bebidas(idd)
                        case "2":
                            os.system('cls')
                            bebidas_crud.exibir_bebidas()
                        case "3":
                            os.system('cls')
                            bebidas_crud.editar_bebida()
                            input("Continuar ")
                        case "4":
                            os.system('cls')
                            bebidas_crud.deletar_bebida()
                        case "0":
                            break          
                        case _:
                            os.system('cls')
                            print("Opção inválida!")
                            Entrada_saida.continuar()
            case "4":
                opcao_brinquedos = " "
                while(opcao_brinquedos != "0"):
                    os.system('cls')
                    opcao_brinquedos = Entrada_saida.menu_brinquedos()
                    os.system('cls')
                    match opcao_brinquedos:
                        case "1":
                            os.system('cls')
                            contador_id += 1
                            idd = contador_id
                            brinquedos_crud.cadastrar_brinquedo(idd)
                        case "2":
                            os.system('cls')
                            brinquedos_crud.exibir_brinquedos()
                        case "3":
                            os.system('cls')
                            brinquedos_crud.editar_brinquedos()
                            input("Continuar ")
                        case "4":
                            os.system('cls')
                            brinquedos_crud.deletar_brinquedo()
                        case "0":
                            break          
                        case _:
                            os.system('cls')
                            print("Opção inválida!")
                            Entrada_saida.continuar()
            case "5":
                os.system('cls')
                print("O mercadinho ")
            case "0":    
                exit()            
            case _:
                os.system('cls')
                print("Opção inválida!")
                Entrada_saida.continuar()