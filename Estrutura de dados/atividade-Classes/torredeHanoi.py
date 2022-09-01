def hanoi(n, A, B, C):
  if(n > 0):
    hanoi(n-1, A, C, B)
    print ("Mova o disco " + str(n) + " de " + A + " para " + B)
    hanoi(n-1, C, B, A)

hanoi(3, 'A', 'B', 'C')
