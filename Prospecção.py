import time

def geraNomes():
    """
    Essa função armazena uma sequência de nomes em uma lista e retorna uma lista de nomes de funcionários, cada um pertencente a uma empresa, e uma lista de empresas
    """
    l1 = []
    l2 = []
    k = 1
    print("""
    Você deve adicionar o nome de um funcionário por vez.
    
    No campo seguinte, digite o nome do domínio da empresa em que ele(a) trabalha (equivale ao nome que vem após o @ no email).
    
    Ao término, digite 0 no campo 'Nome do domínio da empresa'
    """)
    print()
    print()
    #time.sleep(10)
    y = input("Nome do domínio da empresa nº{}: ".format(k))
    x = input("Nome do funcionário: ")
    l1.append(y)
    l2.append(x)
    k+=1
    print()
    print()
    while y != 0:
        y = input("Nome do domínio da empresa nº{}: ".format(k))
        if y == "0":
            break
        else:
            l1.append(y)
            x = input("Nome do funcionário: ")
            l2.append(x)
            k += 1
        print()

    return l1, l2

def geraPadroes(empresas, nomes):

    """
    Essa função recebe uma lista de nomes com sua lista de empresas correspondentes e gera uma lista com série de padrões de email possíveis
    """
    ListaDePadroes = []
    for i in range(0, len(empresas)):
        ListaDePadroes.extend(fazPadrao(empresas[i], nomes[i]))

    return ListaDePadroes


def fazPadrao(empresa, nome):
    padroes = []
    i = nome.split()
    dominio = "@"+empresa+".com"
    p1 = i[0] + "_" + i[-1] + dominio
    padroes.append(p1)

    p2 = i[0] + "." + i[-1] + dominio
    padroes.append(p2)

    p3 = i[0] + dominio
    padroes.append(p3)

    p4 = i[-1] + dominio
    padroes.append(p4)

    p5 = i[0][0] + i[-1] + dominio
    padroes.append(p5)

    p6 = i[0] + i[-1][0] + dominio
    padroes.append(p6)

    p7 = i[0] + i[-1] + dominio
    padroes.append(p7)

    p8 = i[-1] + i[0] + dominio
    padroes.append(p8)

    p9 = i[-1] + "." + i[0] + dominio
    padroes.append(p9)

    p10 = i[-1] + "_" + i[0] + dominio
    padroes.append(p10)

    p11 = i[0] + "." + i[-1] + dominio
    padroes.append(p11)

    p12 = i[0][0] + "." + i[-1] + dominio
    padroes.append(p12)

    p13 = i[0] + "." + i[-1][0] + dominio
    padroes.append(p13)

    p14 = i[0][0] + "." + i[-1] + dominio
    padroes.append(p14)

    p15 = i[0] + "." + i[-1][0] + dominio
    padroes.append(p15)

    p16 = i[0][0] + "_" + i[-1] + dominio
    padroes.append(p16)

    p17 = i[0] + "_" + i[-1][0] + dominio
    padroes.append(p17)

    return padroes


def geraOutput(emails, numeroDeLinhas):
    """
    Essa função gera um output em .txt com a série de padrões de email possíveis
    """
    dia = time.asctime().split()
    data = "{}-{}".format(dia[2], dia[1])


    modo = open(r"PadroesEmail {}.txt".format(data), "w")
    for i in range(0, numeroDeLinhas - 1):
        modo.writelines("{}\n".format(emails[i]))
    modo.close()


def main():
    """
    Essa é a função principal do programa que consiste em gerar uma lista de padrões de email pré-selecionados a partir de uma outra lista de nomes
    """
    ListaDeNomes = []
    ListaDeEmpresas = []
    input = geraNomes()
    ListaDeNomes.extend(input[1])
    ListaDeEmpresas.extend(input[0])

    padroes = geraPadroes(ListaDeEmpresas, ListaDeNomes)

    geraOutput(padroes, len(padroes))


main()