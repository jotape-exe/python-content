def msg():
    print(30*'-')

meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
 "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
#Lista de meses

temp = []
#Lista de temperaturas

for x in range(0, len(meses)):
    temp.append(float(input("TEMPERATURA DE " + meses[x] + " : ")))
    msg()
#Adiciona a temperatura de acordo com o mês

media = sum(temp)/len(temp)
#Média das temperaturas

print('MÉDIA ANUAL:',media)
msg()
print(8*' '+'ACIMA DA MÉDIA')
msg()

for x in range(0, len(temp)):
    if temp[x] > media:
        print (str(x+1) + " - " + meses[x])
        msg()
#Mostra os mêses que a temperatura estava acima da média