def tip():
  print("Hello, respond the question to know how much you have to leve for    a tip ")
  print("How many people")
  a=input()
  print("Ok, now the cost")
  b=input()
  print("And to finish, the percentage you want to give")
  c=input()

  x=(float(c))/100*float(b)
  y=(float(b))+(float(x))
  z=float(x)/float(a)

  print('The original cost was',b)
  print('The total amount to pay is',y)
  
  
  if float(a)>=2:
    print("For each pearson is",z) 
  elif float(a)==1:
    print("The tip is",z)
  elif float(a)<=(-1):
    print('No negative numbers allow')
  else:
    print('No leters or special characters allow')
  
tip()
