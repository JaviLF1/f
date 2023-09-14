def discount():
  print('hello, I am discount bot')
  print('write first the price and then the discount bip-bop')
  print('Price')
  a=input()
  print('discount')
  b=input()

  c=(float(b)/100)*(float(a))
  d=float(a)-float(c)

  print('The total price is',d)
  print('The amount you have save is',c)
  print('The porcentaje you have save is',b,'%')

discount()
