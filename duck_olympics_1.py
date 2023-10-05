def suma (a,b):
  x=a+b
  return x

def resta(a,b):
  x=a-b
  return x

print('dame el primer numero:')
a=(int(input()))
print('dame el segundo')
b=(int(input()))
print('la suma da',suma(a,b),'y la resta da',resta(a,b))


#multiplication and divisi

print('put the first number')
a=(int(input()))
print('put the second one')
b=(int(input()))
def multi(a,b):
  x=a*b
  return x

def division(a,b):
  x=a/b
  return x



print(' la multiplicacion da',multi(a,b),'y la divicion da',division(a,b))



#Unit conversion

print('put here the kilometers that have pass')
kilometers=int(input())

def conversion(kilometers):
  
  meters=kilometers*1000
  return meters
print('you have move',conversion(kilometers),'meters')


#triangle area
print('put here the hinght of the triangle')
height=int(input())
print('and here there base')
base=int(input())

def triangle_area(height,base):
  area=height*base/2
  return area

print('the area is',triangle_area(height,base))
