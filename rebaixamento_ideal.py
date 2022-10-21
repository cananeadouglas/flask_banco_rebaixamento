import math

qtd_m_palestes = int(input("Digite a quantidade máxima de paletes no caminhão: "))
qtd_m_lastro = int(input("Digite a quantidade máxima de caixa por lastro: "))

termopositivo = "y"

qtd_m_empilhamento = int(input("Digite a quantidade máxima de empilhamento por paletes: "))
qtd_m_caixa_por_palete = qtd_m_lastro * qtd_m_empilhamento
print(" ")
print("a quantidade máxima de caixas por palete é (", qtd_m_caixa_por_palete, ")")
teste = input("Você confirma? digite y para sim e n para não ")
print(" ")

menos_1_lastro = qtd_m_empilhamento-1
menos_2_lastro = qtd_m_empilhamento-2
menos_3_lastro = qtd_m_empilhamento-3
print(menos_1_lastro, menos_2_lastro, menos_3_lastro)

if termopositivo == teste:
    #print("continuar")
    compra = int(input("cliente comprou quantos palestes? "))
    print(" ")

    caixa_palete_ideal = qtd_m_caixa_por_palete - qtd_m_lastro
    print("A quantidade de CAIXAS passou a ser: ", caixa_palete_ideal)

    total_caixas_compradas = compra * qtd_m_caixa_por_palete
    #print( "A quantidade Total de CAIXAS é de: ", total_caixas_compradas)

    qtd_lastro_maximo_ideal = total_caixas_compradas / qtd_m_lastro
    #print( 'O total de lastros é {}'.format(math.trunc(qtd_lastro_maximo_ideal)) )

    information01 = qtd_lastro_maximo_ideal / menos_1_lastro
    information02 = qtd_lastro_maximo_ideal / menos_2_lastro
    information03 = qtd_lastro_maximo_ideal / menos_3_lastro

    #print(information01, information02, information03)

    menor = information01
    if information02 < information01 and information02 < information03:
        menor = information02
    if information03 < information01 and information03 < information02:
        menor = information03
    maior = information01
    if information02 > information01 and information02 > information03:
        maior = information02
    if information03 > information01 and information03 > information02:
        maior = information03

    #print('o maior é {} e o menor é {}'.format(maior, menor))

    if  menor > qtd_m_palestes:
        print("nada fazer")
    elif menor <= qtd_m_palestes:
        numero_de_caixas_ideal = caixa_palete_ideal * int('{}'.format(math.trunc(menor)))
        #print(numero_de_caixas_ideal)
        # fim do programa
        saldo = total_caixas_compradas - numero_de_caixas_ideal
        print("A quantidade total de paletes passou a ser: {} ".format(int('{}'.format(math.trunc(menor+1))) ))
        print("sendo que são {} paletes inteiros com {} caixas ".format(math.trunc(menor), caixa_palete_ideal))
        print("e 1 palete com {} caixas".format(saldo))

# fim do programa

elif termopositivo == "n":
    print("vamos tentar novamente?")

else: 
    print("terminando o programa")