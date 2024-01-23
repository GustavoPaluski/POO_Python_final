class Entrada_saida:
    
    # def __init__(self, ):
    
    def escrever_texto(msg):
        print(msg)
        
    def menu_principal():
        print("[1] - Cliente\n[2] - Produtos\n[3] - Bebidas\n[4] - Brinquedos\n[5] - Sobre nós\n[0] - Sair\n")
        return input("-> ")
    
    def menu_cliente():
        print("[1] - Cadastrar Usuário\n[2] - Exibir informações do usuário\n[3] - Editar usuário\n[4] - Deletar cliente\n[0] - Sair")
        opcao = input("Digite uma opcao: ")
        return opcao
    
    def menu_alimentos():
        menu_validacao = False
        print("[1] - Cadastrar alimento\n[2] - Exibir informações do alimento\n[3] - Editar alimento\n[4] - Deletar alimento\n[0] - Sair")
        while(menu_validacao == False):
            try:
                opcao = input("-> ")
                menu_validacao = True
            except:
                print("Apenas números permitidos")
        return opcao
    
    def menu_bebidas():
        menu_validacao = False
        print("[1] - Cadastrar bebida\n[2] - Exibir informações das bebidas\n[3] - Editar bebidas\n[4] - Deletar bebidas\n[0] - Sair")
        while(menu_validacao == False):
            try:
                opcao = input("-> ")
                menu_validacao = True
            except:
                print("Apenas números permitidos")
        return opcao
    
    def menu_brinquedos():
        menu_validacao = False
        print("[1] - Cadastrar brinquedo\n[2] - Exibir informações dos brinquedos\n[3] - Editar brinquedos\n[4] - Deletar brinquedos\n[0] - Sair")
        while(menu_validacao == False):
            try:
                opcao = input("-> ")
                menu_validacao = True
            except:
                print("Apenas números permitidos")
        return opcao

    def continuar():
        input("\nDigite 'ENTER' para continuar: ")