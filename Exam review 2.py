def calor():
  print('Celcious to fahrenheit and kelvin convertor')
  print('Write the celsius')
  a=input()

  f=float(a)*(9/5)+32
  k=float(a)+float(273.15)

  print('Farhrenheit=',int(f))
  print('Kelvins equals =',k)

calor()
