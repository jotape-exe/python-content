meses  = [ "janeiro" ,
         "fevereiro" ,
         "março" ,
         "abril" ,
         "maio" ,
         "junho" ,
         "julho" ,
         "agosto" ,
         "setembro" ,
         "outubro" ,
         "novembro" ,
         "dezembro" ]

dia, mês, ano = input('Data de nascimento: EX: 12/10/2000: ').split('/')

print('Você nasceu em',dia,'de',meses[int(mês) - 1],'de',ano)
