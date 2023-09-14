#easy

def discount():
  print('Easy form')
  print('Oh, hello, I am Juan, and I will be healping you today')
  print('Ok, for our first task, we want to know the price of the')
  print('vibration machine with a discount')
  print('So first I need you te enter the price here')
  a=input()
  print('And the dicount here')
  b=input()

  c=float(b)/100
  d=float(a)*float(c)
  e=float(a)-float(d)

  print('The total amount you have to pay for the vibration machine is',e)

discount()

def machines():
  #normal
  print('Ok, now in the lab they decided that they are going to buy 2 new machines, a temperature machine and a thermal shock machine')
  print('but dont worry, I am here to help you out how much it would be')
  print(' enter here the price of the vibration machine')
  a=input()
  print('here the temperature')
  b=input()
  print('And last the shcok machine')
  c=input()

  d=a+b+c
  e=float(d)*float(.10)
  f=float(d)-float(e)
  print('The price  of all that will be',d,)
  print('But dont worry, the total price with the discount is',f,)

machines()

def convertion():
  #hard
  print('OMG, when I was ready to pay I realize that we have 3 diferent currencies, dolars mexican pesos, and yens')
  print('ok, I just need you to enter they prices again')
  print('vibration')
  a=input()
  print('temperature')
  b=input()
  print('thermal shock')
  c=input()

  d=a+b+c
  e=float(d)*float(8.37)
  g=e*.10
  i=e-g
  

  f=float(d)*float(.057)
  h=f*.10
  j=f-h

  print('the total price in yens is',e)
  print('the total price in dolars is',f)
  print('the total price in yens with the discount is',i)
  print('the total price in dolars with the discount is',j)

convertion()
