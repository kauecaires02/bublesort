# bublesort

num = [3, 1, 4, 5, 2]

troca = True

while troca:
  troca = False
    for n in range(4):
      a  = num[n]
        b = num[n+1]
          if b < a:
    num[n] = b
    num[n+1] = a
    troca = True

print (num)
