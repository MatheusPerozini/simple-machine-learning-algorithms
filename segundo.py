import csv

def carregar_acessos():
    x = []
    y = []

    arquivo = open('acesso.csv','rt')
    leitor  = csv.reader(arquivo)
    next(leitor)
    for acessor_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        x.append([int(acessor_home),int(acessou_como_funciona),int(acessou_contato)])
        y.append(int(comprou))

    return x,y

def carregar_buscas():
    x = []
    y = []

    arquivo  = open('busca.csv','rt')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home,busca,logado,comprou in leitor:
        dados = [int(home),busca,int(logado)]
        x.append(dados)
        y.append(int(comprou))

    return x,y