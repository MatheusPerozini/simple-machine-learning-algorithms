import pandas as pd
dados = pd.read_csv('busca.csv')
y = dados['comprou']
x = dados[['home','busca','logado']]

xdummies= pd.get_dummies(x)
ydummies = y

x = xdummies.values
y = ydummies.values

tamanho_treino = int(0.9 * len(y))

treino_dados = x[:tamanho_treino]
treino_marcacoes = y[:tamanho_treino]

tamanho_teste = len(y) - tamanho_treino

teste_dados = x[-tamanho_teste:]
teste_marcacoes = y[-tamanho_teste:]

acerto_de_um = sum(y)
acerto_de_zero = len(y) - sum(y)
taxa_acerto_base =  100.0 * max(acerto_de_um,acerto_de_zero) / len(y)
print('a taxa foi %f' % taxa_acerto_base)

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)