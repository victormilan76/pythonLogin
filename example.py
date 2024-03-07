'''
Esto es un ejemplo con las funciones 
mas usadas en phyton Wellcome 
'''

#mensaje por pantalla string
'''
message = "Desarrollo de Login"
print(message)
'''

#operaciones matematicas int
'''
number1 = 10
number2 = 2
result = (number1 + number2)+9
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(result)
'''

#operadores de comparacion
'''
print(3 > 7) # false
print(7 >= 3) # true
print(7 == 7) # true
print(7 != 6) # true
print('Milan' == 'Milan') #true
print('Milan' == 'MILAN') #false (sencible)
'''

#operadores de comparacion
'''
stok = input('Ingrese un numero')
stok = int(stok)
print(stok>=5 and stok<=10) 
role = input('Digita el rol =>')
print(role == 'admin' or role == 'seller')
'''

#operador logico not
'''
print(not True)
print(not False)
print ('=>', not (False and False))
print (not (True and True))
'''

#condicionales
'''
if True:
    print('verdad')

dog = input('Cual es tu mascota favorita?')
if dog == 'perro':
    print('tienes buen gusto')
if dog == 'gato':
    print('no es de mi gusto')

stock = int(input('Digita el stock'))
if stock >= 100 and stock <= 1000 :
   print('El stok es correcto')
else:
   print('el stok es incorrecto')
'''