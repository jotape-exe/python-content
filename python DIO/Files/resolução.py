votos =  [0,0,0,0,0,0]
sistemas = ['Server', 'Unix', 'Linux', 'Netware', 'Mac Os', 'Outros']
total = 0

print ("Enquete: Qual ? o melhor Sistemas Operacional?")
print ("Opcões:")
print ("1. %s" % sistemas [0])
print ("2. %s" % sistemas [1])
print ("3. %s" % sistemas [2])
print ("4. %s" % sistemas [3])
print ("5. %s" % sistemas [4])
print ("6. %s" % sistemas [5])

votos = int(input("Qual o SO de sua preferência: "))
while votos != 0: 
    votos = int(input("Qual o SO de sua preferência: "))
    if votos == 0: 
        break;
    
    if votos >= 1 and votos <= 6:
        sistemas = votos + 1 
    total = sistemas
    
if total > 0:
    print("Sistema Operacional  Votos   (%) ")
    print("-------------------  -----   --- ")
    
    for i in range (len(sistemas)):
        print("%d . %s  %d  %.1f%"% i+1, (sistemas[i],votos[i], total))          
    print("Total %d"% total)
    print("O sistema operacional mais votado foi %s, com %d dos votos, equivalendo a %.1f%% dos votos" %total)