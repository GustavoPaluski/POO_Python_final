import os

class Validacao:
    #NÃO SEI SE ESTÁ CERTO
    def verificar_cpf_valido(cpf, cliente_lista):
        tamanho_cpf = len(cpf)

        cpf_invalido = False
        for i in range(11):
            if not cpf[i : i+1].isnumeric():
                cpf_invalido = True

        if tamanho_cpf != 11 or cpf_invalido:
            os.system('cls')
            print("\nCPF inválido\n")
            return False
        else:
            tamanho_lista = len(cliente_lista)
            if tamanho_lista == 0:
                return True
            else:
                for i in range(tamanho_lista):
                    if cliente_lista[i].get_cpf() == cpf:   
                        print("\nCPF já cadastrado!\n")
                        return False
                    else:
                        return True
    
    def validar_try_except(msg, ehInt, ehFloat, ehStr):
        while True:
            valor = input(msg)
            if ehInt:
                try:
                    valor = int(valor)
                    if not (valor < 0 or valor > 150):
                        return valor
                    else:
                        os.system('cls')
                        print("Valor inválido")
                        input("Digite enter para continuar")
                except:
                    os.system('cls')
                    print("Valor inválido")
                    input("Digite enter para continuar")
                    
            if ehFloat:
                try:
                    valor = valor.replace(",",".")
                    valor = float(valor)
                    return valor
                except:
                    os.system('cls')
                    print("Valor inválido")
                    input("Digite enter para continuar")
                    os.system('cls')
            
            if ehStr:
                while valor.isalpha() == False:
                    valor = input(msg)
                    os.system('cls')
                    if valor.isalpha():
                        valor.isalpha() == True
                    else:
                        os.system('cls')
                        print("Informe um nome válido!")
                return valor

    def validar_data_validade():
        data_valida_produto = False
        data_validade_convertida_string = ""
        dia_validade = ""
        mes_validade = ""
        ano_validade = ""
        validade = ""
        while data_valida_produto == False:
            os.system('cls')
            print("(DD/MM/AAAA)")
            remove_barras = "/"
            data_validade = input("Informe uma data de validade: ")
            tamanho_validade_antiga = len(data_validade)
            for i in remove_barras:
                data_validade = data_validade.replace(i,'')
            tamanho_validade_atual = len(data_validade)
            if tamanho_validade_antiga-2 == 8:
                try:
                    data_validade = int(data_validade)

                    if tamanho_validade_atual == 8:
                        data_validade_convertida_string = str(data_validade)
                        dia_validade = data_validade_convertida_string[:2]
                        mes_validade = data_validade_convertida_string[2:4]
                        ano_validade = data_validade_convertida_string[4:8]
                        validade = (f"{dia_validade}/{mes_validade}/{ano_validade}")
                        if(not((int(dia_validade) < 1 or int(dia_validade) > 31) or (int(mes_validade) < 1 or int(mes_validade) > 12)\
                        or (int(ano_validade) < 2000 or int(ano_validade) > 2050))):
                            data_valida_produto = True
                        else:
                            print("Data inválida!")
                            input("Digite 'ENTER' para continuar: ")
                    else:
                        print("Data inválida. A data de Validade precisa ter 8 dígitos")
                        input("Digite 'ENTER' para continuar: ")
                except:
                    print("Data inválida! Digite somente números e barras")
                    input("Digite 'ENTER' para continuar: ")
            else:
                print("Valor inválido!")
                input("Digite 'ENTER' para continuar: ")
        return validade